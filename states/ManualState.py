from parts.driving import DrivingHandler
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton
from parts.remote.RemoteControlListener import RemoteControlListener
from states.State import State


class ManualState(State, RemoteControlListener):
    def __init__(self):
        RemoteControl.add_listener(self)

    def step(self):
        pass

    def deactivate(self):
        RemoteControl.remove_listener(self)

    @staticmethod
    def get_name():
        return "Manual State"

    def on_button_press(self, button):

        # Don't handle mode switches
        if ControllerButton.is_mode_button(button):
            return

        # TODO: Code for handling the arm and gripper

    def on_joystick_change(self, left_amount, right_amount):
        # TODO: Normalize joystick amounts in relation to speed limits
        DrivingHandler.set_speed(left_amount, right_amount)