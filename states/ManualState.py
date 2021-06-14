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
        super().__init__()
        RemoteControl.get_instance().add_listener(self)
        self.speed_multiplier = 1
        if Constants.USING_WEBOTS is False:
            self.speed_multiplier = 1.0
        # Zero is no arm movement, -1 is down and 1 is up
        self.arm_move = 0
        # zero is no gripper movement, -1 open and 1 is close
        self.gripper_move = 0

    def step(self):
        if self.arm_move == -1:
            Arm.get_instance().arm_down()
        elif self.arm_move == 1:
            Arm.get_instance().arm_up()
        self.arm_move = 0

        if self.gripper_move == -1:
            Gripper.get_instance().open_gripper()
        elif self.gripper_move == 1:
            Gripper.get_instance().close_gripper()
        self.gripper_move = 0

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
                self.arm_move = 1

        # Move the arm down
        elif button == ControllerButton.ARM_DOWN:
            if Arm.get_instance().is_up():
                self.arm_move = -1

        # Open the gripper
        elif button == ControllerButton.GRIPPER_OPEN:
            if Gripper.get_instance().get_is_closed():
                self.gripper_move = -1

        # Close the gripper
        elif button == ControllerButton.GRIPPER_CLOSE:
            if not Gripper.get_instance().get_is_closed():
                self.gripper_move = 1

    def on_joystick_change(self, left_amount, right_amount):
        DrivingHandler.set_speed(left_amount * self.speed_multiplier, right_amount * self.speed_multiplier)

    def __del__(self):
        self.deactivate()