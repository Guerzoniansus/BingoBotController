from constants import Constants

from parts.arm import Arm
from parts.driving import DrivingHandler
from parts.gripper import Gripper
from parts.remote.ControllerButton import ControllerButton
from parts.remote.RemoteControl import RemoteControl
from parts.remote.RemoteControlListener import RemoteControlListener
from states.State import State


class ManualState(State, RemoteControlListener):
    def __init__(self):
        RemoteControl.get_instance().add_listener(self)
        self.speed_multiplier = 1
        if Constants.USING_WEBOTS is False:
            # TODO : Correct speed multiplier for real transmissionmotors
            self.speed_multiplier = 0.5

    def step(self, button):
        if ControllerButton.is_mode_button(button):
            return
        if button == ControllerButton.ARM_UP:
            Arm.arm_up()
            print("Arm is going up")
            pass
        elif button == ControllerButton.ARM_DOWN:
            Arm.arm_down()
            print("Arm is going down")
            pass
        elif button == ControllerButton.GRIPPER_OPEN:
            Gripper.open_gripper()
            print("Gripper is being opened")
            pass
        elif button == ControllerButton.GRIPPER_CLOSE:
            Gripper.close_gripper()
            print("Gripper is being closed")
            pass
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

    def on_joystick_change(self, left_amount, right_amount):
        DrivingHandler.set_speed(left_amount * self.speed_multiplier, right_amount * self.speed_multiplier)