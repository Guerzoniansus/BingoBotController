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
            if self.sub_move_start_time == 0:
                DrivingHandler.set_speed(0, 0)
                Gripper.get_instance().up()
            else:
                DrivingHandler.set_speed(0, 0)
                Gripper.get_instance().down()

            self.sub_move_start_time = datetime.now()
            self.sub_move_count += 1
