#include <Arduino.h>
volatile long encCount=0;
const uint8_t ENC_A=2, ENC_B=3, PWM_CW=5, PWM_CCW=6;
unsigned long lastMs=0; long lastCount=0; float rpm=0; const float PPR=600.0f; // set actual counts/rev
void isrA(){ bool a=digitalRead(ENC_A), b=digitalRead(ENC_B); encCount += (a==b)?1:-1; }
void setMotor(int u){ u=constrain(u,-255,255); if(u>0){analogWrite(PWM_CW,u);analogWrite(PWM_CCW,0);}else if(u<0){analogWrite(PWM_CW,0);analogWrite(PWM_CCW,-u);}else{analogWrite(PWM_CW,0);analogWrite(PWM_CCW,0);} }
void setup(){ Serial.begin(115200); pinMode(ENC_A,INPUT_PULLUP); pinMode(ENC_B,INPUT_PULLUP); pinMode(PWM_CW,OUTPUT); pinMode(PWM_CCW,OUTPUT); attachInterrupt(digitalPinToInterrupt(ENC_A),isrA,CHANGE); }
void loop(){
 if(Serial.available()){
   String s=Serial.readStringUntil('\n'); s.trim();
   if(s.startsWith("M,")) setMotor(s.substring(2).toInt());
   else if(s=="Z"){noInterrupts();encCount=0;interrupts();}
   else if(s=="STOP") setMotor(0);
 }
 unsigned long now=millis(); if(now-lastMs>=50){
   noInterrupts(); long c=encCount; interrupts();
   float dt=(now-lastMs)/1000.0f; rpm=(c-lastCount)/PPR/dt*60.0f; lastCount=c; lastMs=now;
   Serial.print("T,");Serial.print(now);Serial.print(',');Serial.print(c);Serial.print(',');Serial.println(rpm,3);
 }
}
