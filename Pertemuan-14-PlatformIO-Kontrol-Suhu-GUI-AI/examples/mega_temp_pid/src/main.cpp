#include <Arduino.h>
#include <PIDCore.h>

static constexpr uint8_t TEMP_PIN=A0;
static constexpr uint8_t SSR_PIN=8;
static constexpr uint32_t CONTROL_MS=200;
static constexpr uint32_t HEARTBEAT_TIMEOUT_MS=2500;

PIDCore pid;
float setpointC=45.0f,kp=5.0f,ki=0.08f,kd=2.0f;
float maxTempC=60.0f;
uint32_t windowMs=2000;
bool running=false;
bool requireHost=true;
uint8_t fault=0;
uint32_t lastPing=0;
uint32_t windowStart=0;

enum FaultCode:uint8_t{OK=0,SENSOR_INVALID=1,OVER_TEMP=2,HOST_TIMEOUT=3,CONFIG_FAULT=5};

void heaterOff(){digitalWrite(SSR_PIN,LOW);}
void stopControl(){running=false;heaterOff();pid.reset();}
void setFault(uint8_t code){fault=code;stopControl();}
void clearFault(){fault=0;pid.reset();lastPing=millis();}

float readTemperatureC(){
  // Average ADC samples to reduce noise. Baseline conversion = LM35, 10 mV/degC.
  uint32_t sum=0;
  for(uint8_t i=0;i<16;i++) sum+=analogRead(TEMP_PIN);
  const float adc=sum/16.0f;
  const float voltage=adc*(5.0f/1023.0f);
  return voltage*100.0f;
}

void printStatus(){
  Serial.print("#STATUS,RUN=");Serial.print(running);
  Serial.print(",FAULT=");Serial.print(fault);
  Serial.print(",SP=");Serial.print(setpointC,3);
  Serial.print(",KP=");Serial.print(kp,4);
  Serial.print(",KI=");Serial.print(ki,4);
  Serial.print(",KD=");Serial.print(kd,4);
  Serial.print(",TMAX=");Serial.print(maxTempC,2);
  Serial.print(",WIN=");Serial.println(windowMs);
}

void handleCommand(String line){
  line.trim(); const int comma=line.indexOf(','); if(comma<0)return;
  String key=line.substring(0,comma); String val=line.substring(comma+1);key.toUpperCase();
  const float f=val.toFloat();

  if(key=="PING"){lastPing=millis();}
  else if(key=="RUN"){
    if(val.toInt()==0){stopControl();}
    else if(fault==0){running=true;pid.reset(readTemperatureC());lastPing=millis();windowStart=millis();}
  }
  else if(key=="CLEAR" && val.toInt()!=0)clearFault();
  else if(key=="SP")setpointC=constrain(f,0.0f,maxTempC-1.0f);
  else if(key=="KP")kp=constrain(f,0.0f,100.0f);
  else if(key=="KI")ki=constrain(f,0.0f,20.0f);
  else if(key=="KD")kd=constrain(f,0.0f,100.0f);
  else if(key=="TMAX"){maxTempC=constrain(f,20.0f,100.0f);if(setpointC>=maxTempC)setpointC=maxTempC-1.0f;}
  else if(key=="WIN")windowMs=constrain((long)f,500L,10000L);
  else if(key=="HOST")requireHost=val.toInt()!=0;
  else if(key=="STATUS")printStatus();

  pid.configure(kp,ki,kd,0.0f,100.0f);
}

void setup(){
  pinMode(SSR_PIN,OUTPUT);heaterOff();
  Serial.begin(115200);Serial.setTimeout(5);
  pid.configure(kp,ki,kd,0.0f,100.0f);
  lastPing=millis();windowStart=millis();
  Serial.println("#PROTO,TEMP_PID,2");
  Serial.println("#ms,temp_C,sp_C,error,P,I,D,pid_pct,ssr,fault");
  printStatus();
}

void loop(){
  while(Serial.available())handleCommand(Serial.readStringUntil('\n'));

  if(running && requireHost && millis()-lastPing>HEARTBEAT_TIMEOUT_MS){
    setFault(HOST_TIMEOUT);
  }

  static uint32_t lastControl=0;
  static float pv=0,output=0;
  static bool ssr=false;
  const uint32_t now=millis();

  if(now-lastControl>=CONTROL_MS){
    const float dt=(now-lastControl)/1000.0f;lastControl=now;
    pv=readTemperatureC();

    if(!isfinite(pv) || pv<-5.0f || pv>150.0f)setFault(SENSOR_INVALID);
    else if(pv>=maxTempC)setFault(OVER_TEMP);

    if(running && fault==0){
      output=pid.update(setpointC,pv,dt);
    }else{
      output=0;heaterOff();ssr=false;
    }

    if(now-windowStart>=windowMs)windowStart=now;
    const uint32_t elapsed=now-windowStart;
    ssr=running && fault==0 && elapsed < (uint32_t)(output*0.01f*windowMs);
    digitalWrite(SSR_PIN,ssr?HIGH:LOW);

    Serial.print(now);Serial.print(',');
    Serial.print(pv,3);Serial.print(',');
    Serial.print(setpointC,3);Serial.print(',');
    Serial.print(setpointC-pv,3);Serial.print(',');
    Serial.print(pid.pTerm(),3);Serial.print(',');
    Serial.print(pid.iTerm(),3);Serial.print(',');
    Serial.print(pid.dTerm(),3);Serial.print(',');
    Serial.print(output,3);Serial.print(',');
    Serial.print(ssr?1:0);Serial.print(',');
    Serial.println(fault);
  }
}
