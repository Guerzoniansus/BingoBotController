from states.State import State
from datetime import datetime
from parts.driving import DrivingHandler
import random


class BingoState(State):
    def __init__(self):
        self.startTime = datetime.now()
        self.bingoNumber = random.randint(1, 75)

    def step(self):
        """" Make a list with numbers that are random added """
        randomList = []
        for randomNumbers in range(1, 75):
            self.bingoNumber = random.randint(1, 75)
            randomList.append(self.bingoNumber)
            print(randomList)

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Bingo State"