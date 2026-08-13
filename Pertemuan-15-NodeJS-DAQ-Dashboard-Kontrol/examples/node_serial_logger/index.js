import fs from 'fs'; import express from 'express'; import {SerialPort} from 'serialport'; import {ReadlineParser} from '@serialport/parser-readline';
const portName=process.argv[2]||'COM5', baud=Number(process.argv[3]||115200); const port=new SerialPort({path:portName,baudRate:baud});const parser=port.pipe(new ReadlineParser({delimiter:'\n'}));
let latest={raw:'waiting'}; const log='data_log.csv'; if(!fs.existsSync(log))fs.writeFileSync(log,'host_time,raw\n');
parser.on('data',line=>{line=line.trim();latest={host_time:new Date().toISOString(),raw:line};fs.appendFileSync(log,`${latest.host_time},"${line}"\n`);console.log(latest);});
const app=express();app.get('/api/latest',(req,res)=>res.json(latest));app.get('/',(req,res)=>res.send(`<h1>Control DAQ</h1><pre id="x">loading</pre><script>setInterval(()=>fetch('/api/latest').then(r=>r.json()).then(v=>x.textContent=JSON.stringify(v,null,2)),500)</script>`));app.listen(3000,()=>console.log('http://localhost:3000'));
