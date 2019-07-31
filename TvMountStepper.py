#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(60)             # 60 RPM

def rotateCounterClockwise():
    print("Single coil steps - Full Revolution Forward (CCW)")
    myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
def rotateClockwise():
    print("Single coil steps - Full Revolution Backward (CW)")
    myStepper.step(200, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.SINGLE)
# myStepper.step(<# of steps>, <direction>, <type of step>
#  ----------------
# | Types of Steps |
#  ----------------
# 1. Single Steps - this is the simplest type of stepping, and uses the
# least power. It uses a single coil to 'hold' the motor in place, as seen
# in the animated GIF above

# 2. Double Steps - this is also fairly simple, except instead of a single
# coil, it has two coils on at once. For example, instead of just coil #1
# on, you would have coil #1 and #2 on at once. This uses more power
# (approx 2x) but is stronger than single stepping (by maybe 25%)

# 3. Interleaved Steps - this is a mix of Single and Double stepping, where
# we use single steps interleaved with double. It has a little more strength
# than single stepping, and about 50% more power. What's nice about this
# style is that it makes your motor appear to have 2x as many steps, for a
# smoother transition between steps

# 4. Microstepping - this is where we use a mix of single stepping with PWM
# to slowly transition between steps. It's slower than single stepping but
# has much higher precision. We recommend 8 microstepping which multiplies
# the # of steps your stepper motor has by 8.

# while (True):
#     print("Single coil steps - Full Revolution Forward & Backward")
#     myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
#     myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

#     print("Double coil steps - Full Revolution Forward & Backward")
#     myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
#     myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

#     print("Interleaved coil steps - Mix of single and double")
#     myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
#     myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

#     print("Microsteps")
#     myStepper.step(200, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
#     myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
