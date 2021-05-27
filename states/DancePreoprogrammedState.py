from enum import Enum
from datetime import datetime

class DancePreprogrammedState:
    def __init__(self):
        pass


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



    def step(self):
        """Step event for this state"""
        x = datetime.datetime.now()

        print(x)

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        pass

    @staticmethod
    def get_name():
        return "Dance Preprogrammed State"