from parts.driving import DrivingHandler
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton


class ManualState:
    def __init__(self):
        RemoteControl.add_listener(self)

    def step(self):
        """Step event for this state"""
        pass

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        RemoteControl.remove_listener(self)

    @staticmethod
    def get_name():
        return "Manual State"

    def on_button_press(self, button):
        """A RemoteControl listener function"""

        # Don't handle mode switches
        if ControllerButton.is_mode_button(button):
            return

        # TODO: Code for handling the arm and gripper

    def on_joystick_change(self, left_amount, right_amount):
        """A RemoteControl listener function"""
        # TODO: Normalize joystick amounts in relation to speed limits
        DrivingHandler.set_speed(left_amount, right_amount)
