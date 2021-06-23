from datetime import datetime
from parts.gripper.Gripper import Gripper
from parts.driving import DrivingHandler


class GripMove:

    def __init__(self, time_for_move):
        self.time_for_move = time_for_move
        self.sub_move_time = time_for_move / 2
        self.sub_move_start_time = datetime.now()
        self.sub_move_count = 0

    def step(self):
        """" If gripper move is called move gripper open and close """
        if ((datetime.now() - self.sub_move_start_time).seconds
                > self.sub_move_time):
            if Gripper.get_instance().get_is_closed():
                Gripper.get_instance().open_gripper()
            else:
                Gripper.get_instance().close_gripper()

            self.sub_move_start_time = datetime.now()
            self.sub_move_count += 1
