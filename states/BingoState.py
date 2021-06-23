from parts.display import Display
from parts.vision import GetBingoCard
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
        self.audioInput = AudioInputHandler.get_instance()
        self.audioInput.add_listener("Bingo", self)
        self.audioOutput = AudioOutputHandler.get_instance()
        self.audioOutput.speak("De bingo begint in 3 2 1 ", "bingo")
        self.audioInput.start_listening()

        self.playingBingo = True
        self._SPEEDS = [4.0, -4.0]


    def step(self):
        """" Make a list with numbers that are random added """
        while len(self.bingoNumberList) > 1 and self.playingBingo is True:
            targetDigit = random.randint(0, len(self.bingoNumberList) - 1)
            Display.show_bingo_number_on_display(targetDigit)
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

    def on_heard(self):
        self.playingBingo = False
        self.audioInput.removeListener(self)
        self.ifBingo()
        pass

    def ifBingo(self):
        self.audioOutput.speak("Houd de kaart voor de camera", "bingo")
        card = GetBingoCard.get_card()
        for row in card:
            for number in row:
                if number in self.bingoNumberList:
                    # False bingo
                    self.audioOutput.speak("Valse bingo, zing nu maar!", "bingo")
                    self.audioOutput.play_berend_botje()
                    self.audioOutput.speak("ha. ha. ha", "bingo")
                    self.audioOutput.speak("We gaan weer verder", "bingo")
                    self.playingBingo = True
                    self.audioInput.add_listener("Bingo", self)
                    return
        # if the code gets here we know that there is a true bingo!!
        print("It was bingo!!!")
        DriveMove(self._SPEEDS[0])

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Bingo State"
