import struct

import numpy as np

from parts.display import Display
from parts.driving import DrivingHandler
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton
from states.State import State
import pyaudio

# Audio setup
CHUNK = 1024 * 4  # number of data points to read at a time
RATE = 44100  # time resolution of the recording device (Hz)
CHANNELS = 1
DEVICE = 1  # device number
LOWEST_FREQUENCY, HIGHEST_FREQUENCY = 8000, 20000
FIRST, SECOND, THIRD, FOURTH, FIFTH = 0, 300, 600, 900, 1200


class DanceAutonomeState(State):

    def __init__(self):
        RemoteControl.add_listener(self)

        p = pyaudio.PyAudio()  # start the PyAudio class
        self.stream = p.open(format=pyaudio.paInt16,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             output=True,
                             frames_per_buffer=CHUNK
                             )  # uses default input device

    np.set_printoptions(suppress=True)  # don't use scientific notation

    def step(self):
        data = struct.unpack(str(CHUNK) + 'h', self.stream.read(CHUNK))
        data = np.array(data)
        data_fft = np.fft.fft(data)
        frequencies = np.fft.fftfreq(len(data_fft))
        highest = np.argpartition(np.abs(data_fft), range(10))[:10]
        print(highest)

        low, mid, high = 0, 0, 0

        for index in highest:
            loudness = np.abs(data_fft[index])
            print("loudness: ", loudness)
            freq = frequencies[index]
            freq = abs(freq * RATE)
            print(freq)

            if freq <= LOWEST_FREQUENCY:  # low frequency sound
                low = self.soundLevel(low, loudness)

            elif freq >= HIGHEST_FREQUENCY:  # high frequency sound
                high = self.soundLevel(high, loudness)

            else:  # otherwise it's middle frequency sound
                mid = self.soundLevel(mid, loudness)

        print("Low: ", low, "   Mid: ", mid, "High: ", high)
        Display.show_vu(low, mid, high)

    def soundLevel(self, level, loudness):
        if loudness < FIRST:
            level = + 1
        elif FIRST <= loudness <= SECOND:
            level = + 2
        elif SECOND < loudness <= THIRD:
            level = + 3
        elif THIRD < loudness <= FOURTH:
            level = + 4
        else:
            level = + 5
        return level

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        DrivingHandler.brake()
        pass

    @staticmethod
    def get_name():
        return "Dance Autonome State"

    def on_button_press(self, button):
        """A RemoteControl listener function"""

        # Don't handle mode switches
        if ControllerButton.is_mode_button(button):
            return
