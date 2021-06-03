# from datetime import datetime
from datetime import datetime

from parts.driving import DrivingHandler


class GripMove:

    def __init__(self, time_for_move):
        self.time_for_move = time_for_move
        self.sub_move_time = time_for_move / 2
        self.sub_move_start_time = datetime.now()
        self.sub_move_count = 0

    def step(self):
        if ((datetime.now() - self.sub_move_start_time).seconds
                > self.sub_move_time):
            if self.sub_move_start_time == 0:
                DrivingHandler.set_speed(0, 0)
                # GripOpen
            else:
                DrivingHandler.set_speed(0, 0)
                # GripClose

            self.sub_move_start_time = datetime.now()
            self.sub_move_count += 1
