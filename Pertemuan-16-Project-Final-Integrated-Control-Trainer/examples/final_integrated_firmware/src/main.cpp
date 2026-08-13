#include <Arduino.h>
#include <max6675.h>

enum Mode : uint8_t { IDLE=0, HEATER=1, MOTOR_SPEED=2, MOTOR_POSITION=3, FAULT=4 };

const uint8_t PWM_CW=5, PWM_CCW=6, ENC_A=2, ENC_B=3, SSR=8;
const uint8_t TC_SCK=52, TC_SO=50, TC_CS=49;
MAX6675 thermocouple(TC_SCK, TC_CS, TC_SO);
volatile long encoderCount=0;
Mode mode=IDLE;
bool runFlag=false;
float sp=0,kp=1,ki=0,kd=0,integral=0,prevError=0,filteredSpeed=0;
float alpha=0.3f; uint16_t sampleMs=100; long prevPos=0; uint32_t lastSample=0,windowStart=0;
const uint32_t HEATER_WINDOW_MS=2000;
float outputCommand=0;

void encISR(){ encoderCount += (digitalRead(ENC_A)==digitalRead(ENC_B)) ? 1 : -1; }
void motorOff(){ analogWrite(PWM_CW,0); analogWrite(PWM_CCW,0); }
void heaterOff(){ digitalWrite(SSR,LOW); }
void allOff(){ motorOff(); heaterOff(); outputCommand=0; }
void resetPID(){ integral=0; prevError=0; }
void setMotor(float u){ int p=constrain((int)lround(u),-255,255); analogWrite(PWM_CW,p>0?p:0); analogWrite(PWM_CCW,p<0?-p:0); }
void zeroPosition(){ noInterrupts();encoderCount=0;interrupts();prevPos=0; }

float pidStep(float error,float dt,float lo,float hi){
  float candidate=integral+error*dt;
  float P=kp*error, I=ki*candidate, D=kd*(error-prevError)/max(dt,0.001f);
  float unsat=P+I+D, out=constrain(unsat,lo,hi);
  if(out==unsat || (out>=hi && error<0) || (out<=lo && error>0)) integral=candidate;
  prevError=error;
  return out;
}

void setMode(Mode next){
  allOff(); resetPID(); mode=next;
  if(mode==MOTOR_POSITION) zeroPosition();
}

void parse(String line){
  line.trim();
  if(line=="START"){runFlag=true;return;}
  if(line=="STOP"){runFlag=false;setMode(IDLE);return;}
  if(line=="ZERO"){zeroPosition();return;}
  int q=line.indexOf('='); if(q<0)return;
  String key=line.substring(0,q), val=line.substring(q+1);
  if(key=="MODE"){
    if(val=="HEATER")setMode(HEATER);
    else if(val=="MOTOR_SPEED")setMode(MOTOR_SPEED);
    else if(val=="MOTOR_POSITION")setMode(MOTOR_POSITION);
    else setMode(IDLE);
    return;
  }
  float v=val.toFloat();
  if(key=="SP")sp=v;
  else if(key=="KP")kp=max(0.0f,v);
  else if(key=="KI")ki=max(0.0f,v);
  else if(key=="KD")kd=max(0.0f,v);
  else if(key=="ALPHA")alpha=constrain(v,0.0f,1.0f);
  else if(key=="TS")sampleMs=constrain((int)v,20,1000);
}

void setup(){
  Serial.begin(115200); pinMode(PWM_CW,OUTPUT);pinMode(PWM_CCW,OUTPUT);pinMode(ENC_A,INPUT_PULLUP);pinMode(ENC_B,INPUT_PULLUP);pinMode(SSR,OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ENC_A),encISR,CHANGE);attachInterrupt(digitalPinToInterrupt(ENC_B),encISR,CHANGE);
  allOff(); lastSample=windowStart=millis();
  Serial.println("# time_ms,mode,sp,pv,output,fault");
}

void loop(){
  if(Serial.available())parse(Serial.readStringUntil('\n'));
  uint32_t now=millis();
  if(now-lastSample>=sampleMs){
    float dt=(now-lastSample)/1000.0f; lastSample=now; bool fault=false; float pv=0;
    if(mode==HEATER){
      motorOff(); pv=thermocouple.readCelsius(); fault=isnan(pv)||pv<0||pv>90||sp>80;
      if(fault){mode=FAULT;runFlag=false;allOff();}
      else outputCommand=runFlag?pidStep(sp-pv,dt,0,100):0;
    }else if(mode==MOTOR_SPEED || mode==MOTOR_POSITION){
      heaterOff(); long p;noInterrupts();p=encoderCount;interrupts();float raw=(p-prevPos)/max(dt,0.001f);prevPos=p;filteredSpeed=alpha*raw+(1-alpha)*filteredSpeed;
      pv=(mode==MOTOR_POSITION)?(float)p:filteredSpeed; outputCommand=runFlag?pidStep(sp-pv,dt,-255,255):0; if(runFlag)setMotor(outputCommand);else motorOff();
    }else{allOff();}
    Serial.print(now);Serial.print(',');Serial.print((int)mode);Serial.print(',');Serial.print(sp);Serial.print(',');Serial.print(pv);Serial.print(',');Serial.print(outputCommand);Serial.print(',');Serial.println(fault?1:0);
  }
  if(mode==HEATER){
    if(now-windowStart>=HEATER_WINDOW_MS)windowStart+=HEATER_WINDOW_MS;
    uint32_t onMs=(uint32_t)(HEATER_WINDOW_MS*constrain(outputCommand,0.0f,100.0f)/100.0f);
    digitalWrite(SSR,(runFlag && (now-windowStart)<onMs)?HIGH:LOW);
  }else heaterOff();
}
