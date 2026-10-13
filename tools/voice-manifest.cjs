const fs=require('fs'),vm=require('vm');const dir=process.argv[2];
const el=()=>({classList:{add(){},remove(){},toggle(){}},dataset:{},style:{},setAttribute(){},querySelectorAll(){return []},querySelector(){return null},insertAdjacentHTML(){}});
const els={};const document={getElementById:id=>els[id]||(els[id]=el()),querySelector:()=>el(),createElement:el,body:{appendChild(){}}};
const ctx=vm.createContext({document,window:{scrollTo(){}},localStorage:{getItem(){return null},setItem(){}},console,setTimeout(){},clearTimeout(){}});
vm.runInContext(fs.readFileSync(dir+'/curriculum.js','utf8')+'\n'+fs.readFileSync(dir+'/app.js','utf8')+'\n;globalThis.__s=clipScript();',ctx);
fs.writeFileSync(process.argv[3],JSON.stringify(ctx.__s));
const all=Object.values(ctx.__s).flat();console.log(Object.keys(ctx.__s).length,'files',all.length,'clips',all.reduce((n,c)=>n+c.text.length,0),'chars');
