#include <Arduino.h>
#include <PIDCore.h>

static constexpr uint8_t PWM_CW=5, PWM_CCW=6, ENC_A=2, ENC_B=3;
static constexpr uint32_t HEARTBEAT_TIMEOUT_MS=2500;
static constexpr uint32_t STALL_TIME_MS=2000;

enum Mode:uint8_t{MODE_SPEED=1,MODE_POSITION=2};
enum Fault:uint8_t{FAULT_OK=0,FAULT_HOST_TIMEOUT=3,FAULT_STALL=4,FAULT_CONFIG=5};

volatile int32_t encoderCount=0;
volatile uint8_t prevState=0;
static const int8_t QDEC[16]={0,-1,1,0, 1,0,0,-1, -1,0,0,1, 0,1,-1,0};

PIDCore pid;
Mode mode=MODE_SPEED;
float setpoint=0.0f;
float kp=0.45f,ki=0.08f,kd=0.002f;
float countsPerRev=600.0f;
float alpha=0.25f;
uint8_t maN=8;
uint16_t sampleMs=20;
uint8_t maxPwm=180;
bool running=false;
bool requireHost=true;
uint8_t fault=FAULT_OK;
uint32_t lastPing=0,stallStarted=0;

float rpmRaw=0,rpmMA=0,rpmLPF=0,positionDeg=0,outputPwm=0;
int pwmCW=0,pwmCCW=0;

// Estimator state is global so ZERO/mode changes can clear all history in a
// controlled way. Keeping lastCount synchronized prevents a false RPM spike.
int32_t lastCount=0;
float rpmRing[16]={0};
uint8_t ringIndex=0,ringSamples=0;

void encoderISR(){
  const uint8_t s=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  encoderCount += QDEC[(prevState<<2)|s];
  prevState=s;
}

int32_t readCount(){
  noInterrupts();
  const int32_t c=encoderCount;
  interrupts();
  return c;
}

void motorWrite(float u){
  const int cmd=(int)constrain(u,-(float)maxPwm,(float)maxPwm);
  if(cmd>0){pwmCW=cmd;pwmCCW=0;analogWrite(PWM_CW,pwmCW);analogWrite(PWM_CCW,0);}
  else if(cmd<0){pwmCW=0;pwmCCW=-cmd;analogWrite(PWM_CW,0);analogWrite(PWM_CCW,pwmCCW);}
  else{pwmCW=pwmCCW=0;analogWrite(PWM_CW,0);analogWrite(PWM_CCW,0);}
}

void stopMotor(){
  running=false;
  outputPwm=0;
  motorWrite(0);
  pid.reset();
  stallStarted=0;
}

void setFault(uint8_t code){fault=code;stopMotor();}

void clearFault(){
  fault=FAULT_OK;
  pid.reset();
  lastPing=millis();
  stallStarted=0;
}

void clearSpeedEstimator(bool zeroEncoder){
  stopMotor();
  noInterrupts();
  if(zeroEncoder)encoderCount=0;
  lastCount=encoderCount;
  interrupts();

  for(uint8_t i=0;i<16;i++)rpmRing[i]=0;
  ringIndex=0;
  ringSamples=0;
  rpmRaw=0;
  rpmMA=0;
  rpmLPF=0;
  positionDeg=zeroEncoder?0.0f:(readCount()/countsPerRev)*360.0f;
  outputPwm=0;
  pwmCW=pwmCCW=0;
  pid.reset(mode==MODE_SPEED?rpmLPF:positionDeg);
}

void configurePid(){
  pid.configure(kp,ki,kd,-(float)maxPwm,(float)maxPwm);
  pid.reset(mode==MODE_SPEED?rpmLPF:positionDeg);
}

void printStatus(){
  Serial.print("#STATUS,RUN=");Serial.print(running);
  Serial.print(",MODE=");Serial.print((int)mode);
  Serial.print(",FAULT=");Serial.print(fault);
  Serial.print(",SP=");Serial.print(setpoint,3);
  Serial.print(",KP=");Serial.print(kp,4);
  Serial.print(",KI=");Serial.print(ki,4);
  Serial.print(",KD=");Serial.print(kd,4);
  Serial.print(",ALPHA=");Serial.print(alpha,3);
  Serial.print(",MA=");Serial.print(maN);
  Serial.print(",TS=");Serial.print(sampleMs);
  Serial.print(",CPR=");Serial.print(countsPerRev,2);
  Serial.print(",MAXPWM=");Serial.println(maxPwm);
}

void handleCommand(String line){
  line.trim();
  const int comma=line.indexOf(',');
  if(comma<0)return;
  String key=line.substring(0,comma),val=line.substring(comma+1);
  key.toUpperCase();
  const float f=val.toFloat();

  if(key=="PING")lastPing=millis();
  else if(key=="RUN"){
    if(val.toInt()==0)stopMotor();
    else if(fault==FAULT_OK){
      running=true;
      lastPing=millis();
      stallStarted=0;
      pid.reset(mode==MODE_SPEED?rpmLPF:positionDeg);
    }
  }
  else if(key=="CLEAR" && val.toInt()!=0)clearFault();
  else if(key=="MODE"){
    stopMotor();
    mode=(val.toInt()==2)?MODE_POSITION:MODE_SPEED;
    setpoint=0;
    clearSpeedEstimator(false);
    configurePid();
  }
  else if(key=="ZERO" && val.toInt()!=0){
    // Reference changes are performed only while stopped. Count, lastCount,
    // MA/LPF history and PID state are reset together.
    setpoint=0;
    clearSpeedEstimator(true);
    configurePid();
  }
  else if(key=="SP")setpoint=constrain(f,-600.0f,600.0f);
  else if(key=="KP"){kp=constrain(f,0.0f,20.0f);configurePid();}
  else if(key=="KI"){ki=constrain(f,0.0f,20.0f);configurePid();}
  else if(key=="KD"){kd=constrain(f,0.0f,20.0f);configurePid();}
  else if(key=="ALPHA")alpha=constrain(f,0.0f,1.0f);
  else if(key=="MA")maN=(uint8_t)constrain(val.toInt(),1,16);
  else if(key=="TS")sampleMs=(uint16_t)constrain(val.toInt(),10,300);
  else if(key=="CPR")countsPerRev=constrain(f,1.0f,100000.0f);
  else if(key=="MAXPWM"){maxPwm=(uint8_t)constrain(val.toInt(),20,255);configurePid();}
  else if(key=="HOST")requireHost=val.toInt()!=0;
  else if(key=="STATUS")printStatus();
}

void setup(){
  pinMode(PWM_CW,OUTPUT);pinMode(PWM_CCW,OUTPUT);motorWrite(0);
  pinMode(ENC_A,INPUT_PULLUP);pinMode(ENC_B,INPUT_PULLUP);
  prevState=(digitalRead(ENC_A)<<1)|digitalRead(ENC_B);
  attachInterrupt(digitalPinToInterrupt(ENC_A),encoderISR,CHANGE);
  attachInterrupt(digitalPinToInterrupt(ENC_B),encoderISR,CHANGE);
  Serial.begin(115200);Serial.setTimeout(5);
  configurePid();
  lastCount=readCount();
  lastPing=millis();
  Serial.println("#PROTO,MOTOR_PID,3");
  Serial.println("#ms,mode,sp,position_deg,rpm_raw,rpm_ma,rpm_lpf,error,P,I,D,pid_pwm,pwm_cw,pwm_ccw,fault");
  printStatus();
}

void loop(){
  while(Serial.available())handleCommand(Serial.readStringUntil('\n'));
  const uint32_t now=millis();

  if(running && requireHost && now-lastPing>HEARTBEAT_TIMEOUT_MS)setFault(FAULT_HOST_TIMEOUT);

  static uint32_t lastSample=0,lastTelemetry=0;
  if(now-lastSample>=sampleMs){
    const float dt=(now-lastSample)/1000.0f;
    lastSample=now;

    const int32_t c=readCount();
    const int32_t dc=c-lastCount;
    lastCount=c;
    positionDeg=(c/countsPerRev)*360.0f;
    rpmRaw=(dc/countsPerRev)*60.0f/dt;

    rpmRing[ringIndex]=rpmRaw;
    ringIndex=(ringIndex+1)%16;
    if(ringSamples<16)ringSamples++;
    const uint8_t n=(maN<ringSamples)?maN:ringSamples;
    float sum=0;
    for(uint8_t k=0;k<n;k++){
      int idx=(int)ringIndex-1-k;
      if(idx<0)idx+=16;
      sum+=rpmRing[idx];
    }
    rpmMA=sum/(n?n:1);
    rpmLPF=alpha*rpmMA+(1.0f-alpha)*rpmLPF;

    const float feedback=(mode==MODE_SPEED)?rpmLPF:positionDeg;
    if(running && fault==FAULT_OK)outputPwm=pid.update(setpoint,feedback,dt);
    else outputPwm=0;
    motorWrite(outputPwm);

    const bool demandHigh=running && abs(outputPwm)>80.0f;
    const bool notMoving=abs(dc)<1;
    const bool needMotion=(mode==MODE_SPEED)?abs(setpoint)>20.0f:abs(setpoint-positionDeg)>8.0f;
    if(demandHigh && notMoving && needMotion){
      if(stallStarted==0)stallStarted=now;
      else if(now-stallStarted>STALL_TIME_MS)setFault(FAULT_STALL);
    }else stallStarted=0;
  }

  if(now-lastTelemetry>=50){
    lastTelemetry=now;
    const float feedback=(mode==MODE_SPEED)?rpmLPF:positionDeg;
    Serial.print(now);Serial.print(',');Serial.print((int)mode);Serial.print(',');
    Serial.print(setpoint,3);Serial.print(',');Serial.print(positionDeg,3);Serial.print(',');
    Serial.print(rpmRaw,3);Serial.print(',');Serial.print(rpmMA,3);Serial.print(',');Serial.print(rpmLPF,3);Serial.print(',');
    Serial.print(setpoint-feedback,3);Serial.print(',');Serial.print(pid.pTerm(),3);Serial.print(',');
    Serial.print(pid.iTerm(),3);Serial.print(',');Serial.print(pid.dTerm(),3);Serial.print(',');
    Serial.print(outputPwm,3);Serial.print(',');Serial.print(pwmCW);Serial.print(',');Serial.print(pwmCCW);Serial.print(',');Serial.println(fault);
  }
}
