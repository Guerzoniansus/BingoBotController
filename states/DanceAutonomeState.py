from parts.driving import DrivingHandler
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton
from states.State import State
from states.moves.ArmMove import ArmMove
from states.moves.DriveMove import DriveMove
from states.moves.GripMove import GripMove
#   import RPi.GPIO as GPIO


class DanceAutonomeState(State):
    def __init__(self):
        RemoteControl.add_listener(self)
        # GPIO.setwarnings(False)  # Ignore warning for now
        # GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        # GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

        self.route_index = 0
        self.song_time = 120

        self._SPEEDS = [
            [7.0, 7.0],  # Forward
            [-7.0, -7.0],  # Backward
            [-4.0, 4.0],  # Left
            [4.0, -4.0]  # Right
        ]

        pass

    def step(self):
        # TODO: code for VU sound action
        # TODO: VU_Meter class
        # if VU_value == HIGH:
        #     GPIO.output(8, GPIO.HIGH)  # Turn on
        #     DriveMove(self._SPEEDS[2]) # Dance to the left
        #     print("Spin to the left")
        #     GPIO.output(8, GPIO.LOW)   # Turn off
        # elif VU_value == MIDDLE:
        #     GPIO.output(9, GPIO.HIGH)  # Turn on
        #     DriveMove(self._SPEEDS[3]) # Dance to the right
        #     print("Spin to the right")
        #     GPIO.output(9, GPIO.LOW)   # Turn off
        # elif VU_value == LOW:
        #     GPIO.output(10, GPIO.HIGH)  # Turn on
        #     ArmMove(self.time_for_move)
        #     print("Move the arm")
        #     GPIO.output(10, GPIO.LOW)   # Turn off

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
