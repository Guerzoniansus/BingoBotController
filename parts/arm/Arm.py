from parts.Ax12 import ax12Servos as servos
import time


left_up = 616
left_down = 923
right_up = 407
right_down = 100


left_servo_ids = [1, 7, 21]
right_servo_ids = [18, 32]


def arm_up():
    __move_arm(left_up, right_up)

def arm_down(self):
    self.move_gripper(self.left_down, self.right_down)

def __move_arm(left_value, right_value):
    for x in left_servo_ids:
        servos.move(x, left_value)
        time.sleep(0.01)
    for x in right_servo_ids:
        servos.move(x, right_value)
        time.sleep(0.01)