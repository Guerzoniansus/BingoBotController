from parts.arm.Arm import Arm
import time

arm = Arm.get_instance()

while True:
    arm.arm_up()
    time.sleep(1)
    arm.arm_down()
    time.sleep(1)
