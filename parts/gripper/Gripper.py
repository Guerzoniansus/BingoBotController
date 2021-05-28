from parts.Ax12 import ax12Servos as servos


close_position = 0
open_position = 300

gripper_id = 5

def close_gripper():
    __move_gripper(close_position)

def open_gripper():
    __move_gripper(open_position)

def __move_gripper(position):
    servos.move(gripper_id, position)
