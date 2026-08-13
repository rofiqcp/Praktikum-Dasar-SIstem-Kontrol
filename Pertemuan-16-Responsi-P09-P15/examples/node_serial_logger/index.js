import { SerialPort } from 'serialport';
import fs from 'node:fs';
const portName=process.argv[2]||'COM5', baud=Number(process.argv[3]||115200);
const port=new SerialPort({path:portName,baudRate:baud});
const out=fs.createWriteStream(`serial_${Date.now()}.csv`);let buf='';
port.on('data',d=>{buf+=d.toString();let i;while((i=buf.indexOf('\n'))>=0){const line=buf.slice(0,i).trim();buf=buf.slice(i+1);if(line){console.log(line);out.write(line+'\n');}}});
process.on('SIGINT',()=>{out.end();port.close(()=>process.exit(0));});
