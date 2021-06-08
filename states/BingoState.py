from states.State import State
from datetime import datetime
import random


class BingoState(State):
    def __init__(self):
        self.startTime = datetime.now()
        self.bingoNumber = random.randint(1, 75)

    def step(self):
        randomList = []
        for randomNumbers in range(1, 75):
            self.bingoNumber = random.randint(1, 75)
            randomList.append(self.bingoNumber)
            print(randomList)

    def deactivate(self):
        pass

    @staticmethod
    def get_name():
        return "Bingo State"