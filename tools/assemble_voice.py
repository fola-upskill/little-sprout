"""Pack recorded lines into one MP3 per module and write voice/index.js with clip timings."""
import json,hashlib,os,subprocess,sys,numpy as np,soundfile as sf
C='.voice-cache';OUT=sys.argv[1];os.makedirs(OUT,exist_ok=True)
man=json.load(open('manifest.json'));SR=24000;GAP=np.zeros(int(.45*SR),dtype=np.float32)
index={};missing=0
for f,clips in man.items():
    parts=[GAP[:int(.1*SR)]];pos=len(parts[0]);index[f]={}
    for c in clips:
        p=f"{C}/{hashlib.sha1(c['text'].encode()).hexdigest()[:16]}.wav"
        if not os.path.exists(p): missing+=1;continue
        a,sr=sf.read(p,dtype='float32');assert sr==SR
        index[f][c['key']]=[round(pos/SR,3),round((pos+len(a))/SR,3)]
        parts+= [a,GAP];pos+=len(a)+len(GAP)
    wav=f'{C}/tmp_{f}.wav';sf.write(wav,np.concatenate(parts),SR)
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',wav,'-ac','1','-ar','24000','-c:a','libmp3lame','-b:a','48k',f'{OUT}/{f}.mp3'],check=True);os.remove(wav)
open(f'{OUT}/index.js','w').write('/* Recorded Storyteller voice (Kokoro af_heart). [start, end] seconds inside voice/<file>.mp3 */\nconst VOICE_CLIPS='+json.dumps(index,separators=(',',':'))+';\n')
print('missing',missing,'files',len(index))
