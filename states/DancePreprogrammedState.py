from datetime import datetime
import random
from states.State import State

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


class DancePreprogrammedState(State):
    def __init__(self):
        """" Set variables for song and time """
        self.dance_start = datetime.now()
        self.song_time = 120
        self._navigator = _Navigator()
        self.nextDirection = 0

        # Which speeds to use for which motors for which directions
        # The first double is the left motor speed, the second double is the right motor speed
        """" Set speed for motors for different directions """
        self._SPEEDS = [
            [70, 70],  # Forward
            [-70, -70],  # Backward
            [-100, 100],  # Left
            [100, -100]  # Right
        ]
        # Set bpm(off song) to set moves on beat of music
        bpm = 109
        self.time_for_move = (bpm / 60) * 2
        self.move_start_time = None
        self.current_move = None
        self.move_choice = None
        self.last_move = None

    def step(self):
        """" If the song is over deactivate the robot """
        if self.dance_start.second + self.song_time < datetime.now().second:
            return self.deactivate()

        # If robot has no move begin with move
        if self.current_move is None:
            self.current_move = DriveMove(self._SPEEDS[0])
            self.move_start_time = datetime.now()
            # print("Seconds")
            # print((self.move_start_time).second)
            # print("time for move in seconds")
            # print(self.time_for_move)

        # If its is time to get new move do new move
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
                # If last move is the same as new move choose a new move
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
