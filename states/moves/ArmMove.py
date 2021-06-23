from datetime import datetime
from parts.arm.Arm import Arm

from parts.driving import DrivingHandler


class ArmMove:

    def __init__(self, time_for_move):
        self.time_for_move = time_for_move
        self.sub_move_time = time_for_move / 2
        self.sub_move_start_time = datetime.now()
        self.sub_move_count = 0

    def step(self):
        """" If arm move is called move arm up and down """
        if ((datetime.now() - self.sub_move_start_time).seconds
                > self.sub_move_time):
            if Arm.get_instance().is_up():
                Arm.get_instance().arm_down()
            else:
                Arm.get_instance().arm_up()

            self.sub_move_start_time = datetime.now()
            self.sub_move_count += 1
