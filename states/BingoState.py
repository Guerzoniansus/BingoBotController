from states.State import State
from parts.driving import DrivingHandler
import random
import time


class BingoState(State):
    def __init__(self):
        self.bingoNumberList = [*range(1, 76, 1)]

    def step(self):
        """" Make a list with numbers that are random added """
        while len(self.bingoNumberList) > 1:
            targetDigit = random.randint(0, len(self.bingoNumberList) - 1)
            # print("bingo list na poppen", bingoNumberList)
            print("remove: ", self.bingoNumberList[targetDigit])
            self.bingoNumberList.pop(targetDigit)
            time.sleep(3)
            # if onheard is True:
            # erik zijn code
            # if bingoCardNumbers is in bingoNumberList:
            # bingo = true #stefan zijn code
            # else:
            # Binog = false


    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Bingo State"