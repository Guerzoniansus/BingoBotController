from enum import Enum
from datetime import datetime
import random

import Constants
from parts.driving import DrivingHandler
from states.moves.DriveMove import DriveMove
from states.moves.ArmMove import ArmMove
from states.moves.GripMove import GripMove

_SECONDS_PER_ROUTE_CHANGE = 1


# class _Direction(Enum):
#     FORWARD = 1
#     BACKWARD = 2
#     LEFT = 3
#     RIGHT = 4
#     ARMUP = 5
#     ARMDOWN = 6
#     GRIPOPEN = 7
#     GRIPCLOSE = 8
#     CIRCLE = 9


class _Navigator:
    """A helper class that determines the pre-programmed routes to take because webots has no remote controller."""
    def __init__(self):
        # self.route = [_Direction.FORWARD, _Direction.BACKWARD, _Direction.LEFT,
        #               _Direction.FORWARD, _Direction.RIGHT, _Direction.BACKWARD]
        self.route_index = 0


class DancePreprogrammedState:
    def __init__(self):
        self.dance_start = datetime.now()
        self.song_time = 206
        self._navigator = _Navigator()
        self.nextDirection = 0

        # Which speeds to use for which motors for which directions
        # The first double is the left motor speed, the second double is the right motor speed
        self._SPEEDS = [
            [7.0, 7.0],
            [-7.0, -7.0],
            [-4.0, 4.0],
            [4.0, -4.0]
        ]
        bpm = 109
        self.time_for_move = (bpm / 60)
        self.move_start_time = None
        self.current_move = None
    # ======================= The actual "do stuff" part of this file

    def step(self):
        if self.dance_start.second + self.song_time < datetime.now().second:
            self.deactivate()
            return
        if self.current_move is None:
            self.current_move = DriveMove(self._SPEEDS[random.randint(0, len(self._SPEEDS)-1)])
            self.move_start_time = datetime.now()
            print("Microseconds")
            print((self.move_start_time).second)
            print("time for move")
            print(self.time_for_move)

        if ((datetime.now() - self.move_start_time).seconds
                > self.time_for_move):
            self.current_move = DriveMove(self._SPEEDS[random.randint(0, len(self._SPEEDS)-1)])
            # self.current_move = ArmMove(self.time_for_move)
            print(self.current_move)
            self.move_start_time = datetime.now()


        self.current_move.step()

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()
        pass

    @staticmethod
    def get_name():
        return "Dance Preprogrammed State"

    # def _change_direction(self):
    #     direction = self._navigator.get_next_direction()
    #     left_speed = self._SPEEDS[direction][0]
    #     right_speed = self._SPEEDS[direction][1]
    #     DrivingHandler.set_speed(left_speed, right_speed)