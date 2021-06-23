import struct

import numpy as np

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
LOWBAR = 100
MIDDLEBAR = 200


class DanceAutonomeState(State):

    def __init__(self):
        RemoteControl.add_listener(self)

        p = pyaudio.PyAudio()  # start the PyAudio class
        stream = p.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK
                        )  # uses default input device

    np.set_printoptions(suppress=True)  # don't use scientific notation

    def step(self):
        data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
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

            if freq <= 8000:  # low frequency sound
                if loudness > LOWBAR:
                    low = + 1
                    print("low lower")
                elif LOWBAR <= loudness <= MIDDLEBAR:
                    low = + 2
                    print("low middle")
                elif loudness > MIDDLEBAR:
                    low = + 3
                    print("low higher")

            elif freq >= 20000:  # high frequency sound
                if loudness > LOWBAR:
                    high = + 1
                    print("high lower")
                elif LOWBAR <= loudness <= MIDDLEBAR:
                    high = + 2
                    print("high middle")
                elif loudness > MIDDLEBAR:
                    high = + 3
                    print("high higher")

            else:  # otherwise it's middle frequency sound
                if loudness > LOWBAR:
                    mid = + 1
                    print("mid lower")
                elif LOWBAR <= loudness <= MIDDLEBAR:
                    mid = + 2
                    print("mid middle")
                elif loudness > MIDDLEBAR:
                    mid = + 3
                    print("mid higher")

        if low != 0:  # when there is low frequencies found light the led amount
            if low == 1:
                print("Low: #")
            elif low == 2:
                print("Low: ##")
            else:
                print("Low: ###")
        if mid != 0:  # when there is middle frequencies found light the led amount
            if mid == 1:
                print("Middle: #")
            elif mid == 2:
                print("Middle: ##")
            else:
                print("Middle: ###")
        if high != 0:  # when there is high frequencies found light the led amount
            if high == 1:
                print("High: #")
            elif high == 2:
                print("High: ##")
            else:
                print("High: ###")

        pass

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
