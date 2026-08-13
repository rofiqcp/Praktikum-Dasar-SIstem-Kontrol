#include <Arduino.h>
const uint8_t ENC_A=2,ENC_B=3; const float CPR=600.0f;
volatile long count=0; unsigned long lastMs=0; long lastCount=0;
void isrA(){ bool a=digitalRead(ENC_A),b=digitalRead(ENC_B); count+=(a==b)?1:-1; }
void setup(){Serial.begin(115200);pinMode(ENC_A,INPUT_PULLUP);pinMode(ENC_B,INPUT_PULLUP);attachInterrupt(digitalPinToInterrupt(ENC_A),isrA,CHANGE);Serial.println("ms,adc,voltage,count,angle_deg,rpm");}
void loop(){unsigned long now=millis();if(now-lastMs>=50){noInterrupts();long c=count;interrupts();float dt=(now-lastMs)/1000.0f;float rpm=(c-lastCount)/CPR/dt*60.0f;int adc=analogRead(A0);float v=adc*(5.0f/1023.0f);float deg=c/CPR*360.0f;Serial.print(now);Serial.print(',');Serial.print(adc);Serial.print(',');Serial.print(v,4);Serial.print(',');Serial.print(c);Serial.print(',');Serial.print(deg,2);Serial.print(',');Serial.println(rpm,3);lastCount=c;lastMs=now;}}
