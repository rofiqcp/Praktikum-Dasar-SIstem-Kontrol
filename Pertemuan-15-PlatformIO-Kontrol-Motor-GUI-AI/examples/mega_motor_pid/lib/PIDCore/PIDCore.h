#pragma once
#include <Arduino.h>

class PIDCore {
 public:
  void configure(float kp, float ki, float kd, float outMin, float outMax) {
    kp_ = kp; ki_ = ki; kd_ = kd; outMin_ = outMin; outMax_ = outMax;
  }

  void reset(float measurement = 0.0f) {
    integral_ = 0.0f;
    prevMeasurement_ = measurement;
    initialized_ = false;
    p_ = i_ = d_ = output_ = 0.0f;
  }

  float update(float setpoint, float measurement, float dt) {
    if (!(dt > 0.0f) || !isfinite(setpoint) || !isfinite(measurement)) {
      output_ = 0.0f;
      return output_;
    }

    const float error = setpoint - measurement;
    p_ = kp_ * error;

    // Derivative on measurement reduces derivative kick at SP changes.
    if (!initialized_) {
      prevMeasurement_ = measurement;
      initialized_ = true;
    }
    d_ = -kd_ * (measurement - prevMeasurement_) / dt;
    prevMeasurement_ = measurement;

    const float candidateI = integral_ + ki_ * error * dt;
    const float rawCandidate = p_ + candidateI + d_;

    // Conditional integration anti-windup.
    const bool highSat = rawCandidate > outMax_;
    const bool lowSat = rawCandidate < outMin_;
    const bool drivesBackFromHigh = highSat && error < 0.0f;
    const bool drivesBackFromLow = lowSat && error > 0.0f;
    if ((!highSat && !lowSat) || drivesBackFromHigh || drivesBackFromLow) {
      integral_ = candidateI;
    }

    i_ = integral_;
    const float raw = p_ + i_ + d_;
    output_ = constrain(raw, outMin_, outMax_);
    return output_;
  }

  float pTerm() const { return p_; }
  float iTerm() const { return i_; }
  float dTerm() const { return d_; }
  float output() const { return output_; }

 private:
  float kp_{0}, ki_{0}, kd_{0};
  float outMin_{-255}, outMax_{255};
  float integral_{0}, prevMeasurement_{0};
  float p_{0}, i_{0}, d_{0}, output_{0};
  bool initialized_{false};
};
