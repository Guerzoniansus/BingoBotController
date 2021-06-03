from datetime import datetime
import random

import Constants
from parts.driving import DrivingHandler
from states.moves.DriveMove import DriveMove
from states.moves.ArmMove import ArmMove
from states.moves.GripMove import GripMove

_SECONDS_PER_ROUTE_CHANGE = 1


class _Navigator:
    """A helper class that determines the pre-programmed routes to take because webots has no remote controller."""
    def __init__(self):
        self.route_index = 0


class DancePreprogrammedState:
    def __init__(self):
        self.dance_start = datetime.now()
        self.song_time = 120
        self._navigator = _Navigator()
        self.nextDirection = 0

        # Which speeds to use for which motors for which directions
        # The first double is the left motor speed, the second double is the right motor speed
        self._SPEEDS = [
            [7.0, 7.0],  # Forward
            [-7.0, -7.0],  # Backward
            [-4.0, 4.0],  # Left
            [4.0, -4.0]  # Right
        ]
        bpm = 109
        self.time_for_move = (bpm / 60) * 2
        self.move_start_time = None
        self.current_move = None
        self.move_choice = None
        self.last_move = None
    # ======================= The actual "do stuff" part of this file

    def step(self):
        if self.dance_start.second + self.song_time < datetime.now().second:
            return self.deactivate()

        if self.current_move is None:
            self.current_move = DriveMove(self._SPEEDS[0])
            self.move_start_time = datetime.now()
            # print("Seconds")
            # print((self.move_start_time).second)
            # print("time for move in seconds")
            # print(self.time_for_move)

        if ((datetime.now() - self.move_start_time).seconds
                > self.time_for_move):
            self.move_choice = random.randint(0, 2)
            print(self.move_choice)
            if self.move_choice == 0 and self.last_move != 0:
                self.current_move = DriveMove(self._SPEEDS[random.randint(0, len(self._SPEEDS)-1)])
                self.last_move = 0
            elif self.move_choice == 1 and self.last_move != 1:
                self.current_move = ArmMove(self.time_for_move)
                self.last_move = 1
            elif self.move_choice == 2 and self.last_move != 2:
                self.current_move = GripMove(self.time_for_move)
                self.last_move = 2
            else:
                if self.last_move == 2:
                    self.current_move = ArmMove(self.time_for_move)
                    self.last_move = 1
                else:
                    self.current_move = GripMove(self.time_for_move)
                    self.last_move = 2

            self.move_start_time = datetime.now()

        self.current_move.step()

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Dance Preprogrammed State"
