from datetime import datetime

from parts.driving import DrivingHandler


class ArmMove:

    def __init__(self, time_for_move):
        self.time_for_move = time_for_move
        self.sub_move_time = time_for_move / 4
        self.sub_move_start_time = datetime.now()
        self.sub_move_count = 0

    def step(self):

        if ((datetime.now() - self.sub_move_start_time).seconds
                > self.sub_move_time):
            if self.sub_move_count == 0:
                DrivingHandler.set_speed(0, 0)
                # arm.up()
            elif self.sub_move_count == 1:
                DrivingHandler.set_speed(1, 1)
            elif self.sub_move_count == 2:
                DrivingHandler.set_speed(0, 0)
                # arm.down()
            else:
                DrivingHandler.set_speed(-1, -1)

            self.sub_move_start_time = datetime.now()
            self.sub_move_count += 1
