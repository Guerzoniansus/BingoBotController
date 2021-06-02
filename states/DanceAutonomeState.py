from parts.driving import DrivingHandler
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton
from states.State import State
from states.moves.ArmMove import ArmMove
from states.moves.DriveMove import DriveMove
from states.moves.GripMove import GripMove


class _Navigator:
    """A helper class that determines the pre-programmed routes to take because webots has no remote controller."""

    def __init__(self):
        self.route_index = 0


class DanceAutonomeState(State):
    def __init__(self):
        RemoteControl.add_listener(self)
        self._navigator = _Navigator()

        self._SPEEDS = [
            [7.0, 7.0],  # Forward
            [-7.0, -7.0],  # Backward
            [-4.0, 4.0],  # Left
            [4.0, -4.0]  # Right
        ]

        self.current_move = None
        self.move_choice = None
        self.time_for_move = (bpm / 60) * 2
        pass

    def step(self):
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

    # def on_sound_change(self, VU_value):
    #     """VU listener function"""
    #     # TODO: code for VU sound action
    #     if VU_value == HIGH
    #         DriveMove(self._SPEEDS[2])
    #         print("Spin to the left")
    #     elif VU_value == MIDDLE
    #         DriveMove(self._SPEEDS[3])
    #         print("Spin to the right")
    #     elif VU_value == LOW
    #         ArmMove(self.time_for_move)
    #         print("Move the arm")
