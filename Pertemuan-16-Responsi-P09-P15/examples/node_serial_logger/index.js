import { SerialPort } from 'serialport';
import fs from 'node:fs';
const portName=process.argv[2];
if(!portName){console.error('Usage: node index.js COM5 [baud]');process.exit(2)}
const baud=Number(process.argv[3]||115200);const port=new SerialPort({path:portName,baudRate:baud});
const file=`serial_${new Date().toISOString().replace(/[:.]/g,'-')}.csv`;const out=fs.createWriteStream(file,{flags:'a'});let buf='';
port.on('open',()=>{port.write('RUN,0\n');port.write('STATUS,1\n');console.log('safe logger open',portName,'->',file)});
port.on('data',data=>{buf+=data.toString();let i;while((i=buf.indexOf('\n'))>=0){const line=buf.slice(0,i).trim();buf=buf.slice(i+1);if(!line||line.startsWith('#'))continue;out.write(line+'\n');console.log(line)}});
const stop=()=>{try{port.write('RUN,0\n')}catch{};setTimeout(()=>{out.end();port.close(()=>process.exit(0))},100)};
process.on('SIGINT',stop);process.on('SIGTERM',stop);
