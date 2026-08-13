#include <Arduino.h>

const uint8_t PIN_PWM_CW = 5;
const uint8_t PIN_PWM_CCW = 6;
const uint8_t PIN_ENC_A = 2;
const uint8_t PIN_ENC_B = 3;

volatile long encoderCount = 0;

float kp = 1.0f, ki = 0.0f, kd = 0.0f;
float setpoint = 0.0f;
float integralTerm = 0.0f, previousError = 0.0f;
float alpha = 0.30f;
float lowPassSpeed = 0.0f;
uint16_t sampleMs = 50;
bool positionMode = false;
bool runFlag = false;

long previousPosition = 0;
uint32_t lastSample = 0;

constexpr uint8_t MA_N = 5;
float speedBuffer[MA_N] = {0};
uint8_t speedIndex = 0;
uint8_t speedCount = 0;

void encoderISR() {
  encoderCount += (digitalRead(PIN_ENC_A) == digitalRead(PIN_ENC_B)) ? 1 : -1;
}

void driveMotor(float command) {
  int pwm = constrain((int)lround(command), -255, 255);
  analogWrite(PIN_PWM_CW, pwm > 0 ? pwm : 0);
  analogWrite(PIN_PWM_CCW, pwm < 0 ? -pwm : 0);
}

float movingAverage(float x) {
  speedBuffer[speedIndex] = x;
  speedIndex = (speedIndex + 1) % MA_N;
  if (speedCount < MA_N) speedCount++;
  float sum = 0.0f;
  for (uint8_t i = 0; i < speedCount; ++i) sum += speedBuffer[i];
  return sum / max((uint8_t)1, speedCount);
}

void resetController() {
  integralTerm = 0.0f;
  previousError = 0.0f;
}

void zeroPosition() {
  noInterrupts();
  encoderCount = 0;
  interrupts();
  previousPosition = 0;
}

void parseCommand(String line) {
  line.trim();
  if (line == "START") { runFlag = true; return; }
  if (line == "STOP") { runFlag = false; driveMotor(0); resetController(); return; }
  if (line == "ZERO") { zeroPosition(); resetController(); return; }

  int q = line.indexOf('=');
  if (q < 0) return;
  String key = line.substring(0, q);
  float value = line.substring(q + 1).toFloat();

  if (key == "SP") setpoint = value;
  else if (key == "KP") { kp = constrain(value, 0.0f, 3.0f); if (kp == 0) previousError = 0; }
  else if (key == "KI") { ki = constrain(value, 0.0f, 3.0f); if (ki == 0) integralTerm = 0; }
  else if (key == "KD") { kd = constrain(value, 0.0f, 3.0f); }
  else if (key == "ALPHA") alpha = constrain(value, 0.0f, 1.0f);
  else if (key == "TS") sampleMs = constrain((int)value, 10, 300);
  else if (key == "MODE") {
    positionMode = ((int)value) == 1;
    resetController();
    if (positionMode) zeroPosition();
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(PIN_PWM_CW, OUTPUT);
  pinMode(PIN_PWM_CCW, OUTPUT);
  pinMode(PIN_ENC_A, INPUT_PULLUP);
  pinMode(PIN_ENC_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(PIN_ENC_A), encoderISR, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_ENC_B), encoderISR, CHANGE);
  driveMotor(0);
  lastSample = millis();
  Serial.println("# time_ms,sp,pos,raw_speed,ma_speed,lpf_speed,feedback,error,p,i,d,output,mode");
}

void loop() {
  if (Serial.available()) parseCommand(Serial.readStringUntil('\n'));

  uint32_t now = millis();
  if (now - lastSample < sampleMs) return;
  float dt = (now - lastSample) / 1000.0f;
  lastSample = now;

  long position;
  noInterrupts();
  position = encoderCount;
  interrupts();

  float rawSpeed = (position - previousPosition) / max(dt, 0.001f);
  previousPosition = position;
  float maSpeed = movingAverage(rawSpeed);
  lowPassSpeed = alpha * maSpeed + (1.0f - alpha) * lowPassSpeed;

  float feedback = positionMode ? (float)position : lowPassSpeed;
  float error = setpoint - feedback;

  float pTerm = (kp == 0.0f) ? 0.0f : kp * error;
  float candidateIntegral = (ki == 0.0f) ? 0.0f : integralTerm + error * dt;
  float iTerm = ki * candidateIntegral;
  float dTerm = (kd == 0.0f) ? 0.0f : kd * (error - previousError) / max(dt, 0.001f);
  float unsaturated = pTerm + iTerm + dTerm;
  float output = constrain(unsaturated, -255.0f, 255.0f);

  // Conditional-integration anti-windup.
  bool notSaturated = (output == unsaturated);
  bool unwinding = (output >= 255.0f && error < 0.0f) || (output <= -255.0f && error > 0.0f);
  if (ki != 0.0f && (notSaturated || unwinding)) integralTerm = candidateIntegral;
  if (ki == 0.0f) integralTerm = 0.0f;
  iTerm = ki * integralTerm;
  previousError = error;

  if (runFlag) driveMotor(output); else driveMotor(0);

  Serial.print(now); Serial.print(',');
  Serial.print(setpoint); Serial.print(',');
  Serial.print(position); Serial.print(',');
  Serial.print(rawSpeed); Serial.print(',');
  Serial.print(maSpeed); Serial.print(',');
  Serial.print(lowPassSpeed); Serial.print(',');
  Serial.print(feedback); Serial.print(',');
  Serial.print(error); Serial.print(',');
  Serial.print(pTerm); Serial.print(',');
  Serial.print(iTerm); Serial.print(',');
  Serial.print(dTerm); Serial.print(',');
  Serial.print(output); Serial.print(',');
  Serial.println(positionMode ? 1 : 0);
}
