"""Record every Storyteller line with Kokoro TTS (voice af_heart). Resumable: finished lines are cached."""
import json,hashlib,os,sys,time,numpy as np,soundfile as sf
from kokoro_onnx import Kokoro
# Run from the project folder. Model files: set KOKORO_DIR (default: tools/).
D=os.environ.get('KOKORO_DIR','tools');C='.voice-cache';os.makedirs(C,exist_ok=True)
man=json.load(open('manifest.json'))
texts=sorted({c['text'] for f in man.values() for c in f})
k=Kokoro(D+'/kokoro-v1.0.onnx',D+'/voices-v1.0.bin')
def norm(t): return t.replace('’',"'").replace('“','"').replace('”','"')
t0=time.time()
for n,t in enumerate(texts):
    h=hashlib.sha1(t.encode()).hexdigest()[:16];out=f'{C}/{h}.wav'
    if os.path.exists(out): continue
    a,sr=k.create(norm(t),voice='af_heart',speed=0.92,lang='en-us')
    # trim quiet edges, keep a tiny natural lead-in/tail
    idx=np.where(np.abs(a)>0.01)[0]
    if len(idx): a=a[max(0,idx[0]-int(.03*sr)):min(len(a),idx[-1]+int(.08*sr))]
    sf.write(out+'.tmp.wav',a,sr);os.replace(out+'.tmp.wav',out)
    if n%25==0: print(n,len(texts),round(time.time()-t0),flush=True)
print('DONE',len(texts),round(time.time()-t0),flush=True)
