from states.State import State
from parts.audio.input.AudioListener import AudioListener
from parts.audio.output.AudioOutputHandler import AudioOutputHandler
from parts.audio.input.AudioInputHandler import AudioInputHandler
from parts.driving import DrivingHandler
from states.moves.DriveMove import DriveMove

import random
import time


class BingoState(State, AudioListener):

    def __init__(self):
        self.bingoNumberList = [*range(1, 76, 1)]
        self.audioInput = AudioInputHandler.getInstance()
        self.audioInput.addListener("Bingo", self)
        self.audioOutput = AudioOutputHandler.get_instance()
        self.audioOutput.speak("De bingo begint in 3 2 1 ", "bingo")
        self.audioInput.startListening()

        self.playingBingo = True
        self._SPEEDS = [4.0, -4.0]


    def step(self):
        """" Make a list with numbers that are random added """
        while len(self.bingoNumberList) > 1 and self.playingBingo is True:
            targetDigit = random.randint(0, len(self.bingoNumberList) - 1)
            self.audioOutput.speak(str(targetDigit), "bingo")
            # print("bingo list na poppen", bingoNumberList)
            print("remove: ", self.bingoNumberList[targetDigit])
            self.bingoNumberList.pop(targetDigit)

            time.sleep(5)
            # if onheard is True:
            # erik zijn code
            # if bingoCardNumbers is in bingoNumberList:
            # bingo = true #stefan zijn code
            # else:
            # Binog = false

    def onHeard(self):
        self.playingBingo = False
        self.audioInput.stopListening()
        pass

    def ifBingo(self):
        if cardNumbers in self.bingoNumberList:
            # False bingo!
        else:
            # True bingo!
            DriveMove(self._SPEEDS[0])  # If bingo is correct make a left circle for joy.
        pass

    # def falseBingo(self):
    #     pass

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Bingo State"
