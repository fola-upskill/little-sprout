const fs=require('fs'),vm=require('vm'),assert=require('assert');
const elements=new Map();let printHTML='',saved='';
function element(){return {textContent:'',innerHTML:'',style:{},dataset:{},disabled:false,classList:{add(){},remove(){},toggle(){}},setAttribute(){},insertAdjacentHTML(){},querySelectorAll(){return []},querySelector(){return null},remove(){},click(){}};}
const document={getElementById(id){if(!elements.has(id))elements.set(id,element());return elements.get(id);},querySelector(s){if(s==='.brand'){if(!elements.has(s))elements.set(s,element());return elements.get(s);}return null;},createElement(){return element();},body:{appendChild(e){printHTML=e.innerHTML;}}};
const context=vm.createContext({document,window:{scrollTo(){},print(){}},localStorage:{getItem(){return null;},setItem(k,v){saved=v;}},console,setTimeout(){return 1;},clearTimeout(){},Blob,URL,confirm(){return true;}});
vm.runInContext(fs.readFileSync('dist/curriculum.js','utf8')+'\n'+fs.readFileSync('dist/voice/index.js','utf8')+'\n'+fs.readFileSync('dist/app.js','utf8'),context);
const run=s=>vm.runInContext(s,context);
assert.equal(run('curriculum.length'),150);
for(const subject of ['math','english','science'])assert.equal(run(`curriculum.filter(m=>m.subject==='${subject}').length`),50);
run(`for(const m of curriculum){if(m.questions.length!==3||m.review.length!==2)throw Error('question count');for(const q of [...m.questions,...m.review]){if(!q.options.includes(q.answer)||new Set(q.options).size!==q.options.length)throw Error('answer choices');}for(const q of m.review){const source=curriculum.find(x=>x.id===q.sourceId);if(!source||source.subject!==m.subject||source.number>m.number)throw Error('review ordering');}}`);
assert.equal(run("available(curriculum.find(m=>m.id==='math-2'))"),false);
run("begin('math-1'); session.step='quiz';");
// A wrong first choice followed by correction never earns a first-choice point.
run(`answer(session.questions[0].options.findIndex(x=>x!==session.questions[0].answer),document.createElement('button'));answer(session.questions[0].options.indexOf(session.questions[0].answer),document.createElement('button'));`);
assert.equal(run('session.score'),0);assert.equal(run('session.wrong.length'),1);
run("session.score=3;session.activity=true;finish();");
assert.equal(run("mastered('math-1')"),false);assert.equal(run("available(curriculum.find(m=>m.id==='math-2'))"),false);
// Exercise real scoring and completion for every module in every subject.
run(`for(const m of curriculum){begin(m.id);if(session.m.id!==m.id)throw Error('unlock');session.step='quiz';for(let i=0;i<5;i++){session.index=i;session.first=true;session.answered=false;answer(session.questions[i].options.indexOf(session.questions[i].answer),document.createElement('button'));}if(session.score!==5)throw Error('score');session.activity=true;finish();if(!mastered(m.id))throw Error('mastery');}`);
assert.equal(run('count()'),150);assert.equal(run('validState(state)'),true);
assert.equal(Object.keys(JSON.parse(saved).records).length,150);
run("begin('math-1');session.score=0;session.activity=true;finish();");assert.equal(run("mastered('math-1')"),true);assert.equal(run("record('math-1').best"),5);
const attempts=run("record('english-50').attempts");run("begin('english-50',true);session.score=5;session.activity=true;finish();");assert.equal(run("record('english-50').attempts"),attempts);
assert.equal(run('validState({records:{bad:{}}})'),false);
run("worksheet(curriculum.find(m=>m.id==='science-50'))");assert(printHTML.includes('GROWN-UP ANSWER KEY'));assert.equal((printHTML.match(/class="print-question"/g)||[]).length,5);
run("subject='science';setView('path');setView('parent');setView('home');");
// Writing voice: no number/plural mismatches anywhere in the curriculum.
assert.equal(run(`JSON.stringify(curriculum).match(/\\b1 (dots|blocks|objects|circles|toys|things)\\b|There are 1\\b/g)`),null);
// Comparison questions offer the numbers being compared.
assert(run(`curriculum.find(m=>m.id==='math-11').questions[0].options.includes('3')`));
// Read-aloud voice: screen text becomes natural spoken words.
assert.equal(run(`speakable('Count the dots: ● ● ● ')`),'Count the dots you see.');
assert.equal(run(`speakable('Fill the gap: 2, 3, __, 5')`),'Fill the gap: 2, 3, blank, 5');
assert.equal(run(`speakable('5 + __ = 10')`),'5 plus what makes 10?');
assert.equal(run(`speakable('red, blue, red, blue, ...')`),'red, blue, red, blue. What comes next?');
assert.equal(run(`speakChoice('?',{prompt:'Choose the mark',options:['.','?',',']})`),'question mark');
assert.equal(run(`speakChoice('a',{prompt:'Which is small A?',options:['a','b','d']})`),'small letter a');
assert.equal(run(`curriculum.flatMap(m=>m.questions).filter(q=>/[_●]|\\.\\.\\./.test(speakable(q.prompt))).length`),0);
// Voice choice prefers natural English voices and skips novelty voices.
assert(run(`voiceScore({name:'Microsoft Aria Online (Natural)',lang:'en-US'})>voiceScore({name:'Microsoft David',lang:'en-US'})`));
assert(run(`SKIP_VOICES.test('Fred')&&!SKIP_VOICES.test('Samantha')`));
// Storyteller recordings: every spoken line has a recording, and each audio file exists.
run(`for(const [f,clips] of Object.entries(clipScript())){if(!VOICE_CLIPS[f])throw Error('no audio file entry '+f);for(const c of clips){const r=VOICE_CLIPS[f][c.key];if(!r||!(r[1]>r[0]))throw Error('missing recording '+f+':'+c.key);}}`);
for(const f of Object.keys(run('VOICE_CLIPS')))assert(fs.statSync('dist/voice/'+f+'.mp3').size>1000,'audio file '+f);
// Review questions point to the recording of their original question.
run(`for(const m of curriculum)for(const q of m.review){const r=questionRef(q);if(r.j<0||r.m.id!==q.sourceId)throw Error('review recording '+m.id);}`);
// Entry screen: names are cleaned and kept only in this browser; greetings use recordings when available.
assert.equal(run(`cleanName('  fanu  ')`),'Fanu');assert(!/[<>!]/.test(run(`cleanName('<b>Ada</b>!!')`)));
assert.equal(run(`cleanChild({name:'Fife',gender:'girl'}).gender`),'girl');assert.equal(run(`cleanChild({name:'',gender:'boy'}).gender`),'');
run(`state.child={name:'Fanu',gender:'boy'};`);assert.equal(run(`greetParts(false)[0].clip`),'common:hi-fanu');
run(`state.child={name:'Zara',gender:'girl',color:'blue'};`);assert.equal(run(`greetParts(true)[0].clip`),'common:back-friend');assert.equal(run(`cleanChild({name:'Zara',gender:'girl',color:'teal'}).color`),'');
// Every spoken part on every screen has a Storyteller recording.
run(`for(const p of [...greetParts(false),...greetParts(true)])if(!clipRange(p.clip))throw Error('greeting without recording '+p.clip);`);assert.equal(run(`greetParts(true)[1].clip`),'common:backRest');
run("setView('entry');setView('hello');setView('parent');setView('home');");
console.log('PASS: 150 modules, 750 question placements, review ordering, scoring, unlocks, retries, mastery retention, preview isolation, saved progress, validation, and worksheet content, curriculum wording, read-aloud speech rules, Storyteller recordings, and the welcome screens.');
