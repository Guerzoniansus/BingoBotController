import time
from parts.gripper.Gripper import Gripper

gripper = Gripper.get_instance()

while True:
    gripper.close_gripper()
    time.sleep(1)
    gripper.open_gripper()
    time.sleep(1)
