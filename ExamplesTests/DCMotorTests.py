import time
from adafruit_motorkit import MotorKit

print("[INFO]: Initialize Motorkit")
kit = MotorKit()

print("[INFO]: Begining stepper enginge test.")
for i in range(100):
    kit.stepper1.onestep()
print("[INFO: Finished engine test.")

