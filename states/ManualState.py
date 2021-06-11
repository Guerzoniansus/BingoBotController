import Constants
from logger.Logger import Logger
#from parts.arm.Arm import Arm
from parts.arm.Arm import Arm
from parts.driving import DrivingHandler
from parts.gripper.Gripper import Gripper
from parts.remote.ControllerButton import ControllerButton
from parts.remote.RemoteControl import RemoteControl
from parts.remote.RemoteControlListener import RemoteControlListener
from states.State import State


class ManualState(State, RemoteControlListener):
    def __init__(self):
        RemoteControl.get_instance().add_listener(self)
        self.speed_multiplier = 1
        if Constants.USING_WEBOTS is False:
            self.speed_multiplier = 1.0

    def step(self):
        pass


    def deactivate(self):
        RemoteControl.get_instance().remove_listener(self)

    @staticmethod
    def get_name():
        return "Manual State"

    def on_button_press(self, button):

        # Don't handle mode switches
        if ControllerButton.is_mode_button(button):
            return

        # Move the arm up
        if button == ControllerButton.ARM_UP:
            if not Arm.get_instance().is_up():
                Arm.get_instance().arm_up()
                Logger.get_instance().log("Arm is going up")

        # Move the arm down
        elif button == ControllerButton.ARM_DOWN:
            if Arm.get_instance().is_up():
                Arm.get_instance().arm_down()
                Logger.get_instance().log("Arm is going down")

        # Open the gripper
        elif button == ControllerButton.GRIPPER_OPEN:
            Gripper.get_instance().open_gripper()
            Logger.get_instance().log("Gripper is being opened")

        # Close the gripper
        elif button == ControllerButton.GRIPPER_CLOSE:
            Gripper.get_instance().get_close_gripper()
            Logger.get_instance().log("Gripper is being closed")

    def on_joystick_change(self, left_amount, right_amount):
        DrivingHandler.set_speed(left_amount * self.speed_multiplier, right_amount * self.speed_multiplier)

    def __del__(self):
        self.deactivate()