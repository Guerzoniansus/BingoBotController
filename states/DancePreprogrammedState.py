from enum import Enum
from datetime import datetime
import random

import Constants
from parts.driving import DrivingHandler
from states.moves.DriveMove import DriveMove
from states.moves.ArmMove import ArmMove
from states.moves.CircleMove import CircleMove
from states.moves.GripMove import GripMove

_SECONDS_PER_ROUTE_CHANGE = 1


class _Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    ARMUP = 5
    ARMDOWN = 6
    GRIPOPEN = 7
    GRIPCLOSE = 8
    CIRCLE = 9


class _Navigator:
    """A helper class that determines the pre-programmed routes to take because webots has no remote controller."""
    def __init__(self):
        self.route = [_Direction.FORWARD, _Direction.BACKWARD, _Direction.LEFT,
                      _Direction.FORWARD, _Direction.RIGHT, _Direction.BACKWARD]
        self.route_index = 0

    # def get_next_direction(self):
    #     """Returns the next Direction to drive to."""
    #     Moves = ["Forward", "Backward", "Left", "Right", "ArmUp", "ArmDown", "GripOpen", "GripClose", "Circle"]
    #     NextMove = random.choice(Moves)
    #     print(NextMove)
    #     return NextMove

        # if self.route_index + 1 < len(self.route):
        #     self.route_index = self.route_index + 1
        # else:
        #     self.route_index = 0
        #
        # return self.route[self.route_index]


class DancePreprogrammedState:
    def __init__(self):
        self._navigator = _Navigator()
        self.nextDirection = 0

        # Which speeds to use for which motors for which directions
        # The first double is the left motor speed, the second double is the right motor speed
        self._SPEEDS = {
            _Direction.FORWARD: [7.0, 7.0],
            _Direction.BACKWARD: [-7.0, -7.0],
            _Direction.LEFT: [-4.0, 4.0],
            _Direction.RIGHT: [4.0, -4.0]
        }
        bpm = 109
        self.time_for_move = (bpm / 60) * 4
        self.move_start_time = None
        self.current_move = None
    # ======================= The actual "do stuff" part of this file

    def step(self):
        if self.current_move is None:
            self.current_move = DriveMove(self._SPEEDS[_Direction.LEFT])
            self.move_start_time = datetime.now()
            print("Microseconds")
            print((self.move_start_time).second)
            print("time for move")
            print(self.time_for_move)

        if ((datetime.now() - self.move_start_time).seconds
                > self.time_for_move):
            self.current_move = DriveMove(self._SPEEDS[_Direction.FORWARD])
            self.move_start_time = datetime.now()
            self.nextDirection = _Direction(random.randint(1, 9))
            print(self.nextDirection)


        self.current_move.step()

    # def get_next_direction(self):
    #     """Returns the next Direction to drive to."""
    #     return random.randint(0, 8)

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