from enum import Enum


class ControllerButton(Enum):
    BINGO = 1
    MANUAL = 2
    DANCE_AUTONOME = 3
    DANCE_PREPROGRAMMED = 4
    AUTONOME_ROUTE = 5
    FAULT = 6
    SHUTDOWN = 7
    ARM_UP = 8
    ARM_DOWN = 9
    GRIPPER_OPEN = 10
    GRIPPER_CLOSE = 11

    @staticmethod
    def is_mode_button(button):
        """Returns true if the button is a switch mode button."""
        return button == ControllerButton.BINGO or button == ControllerButton.MANUAL \
               or button == ControllerButton.DANCE_AUTONOME or button == ControllerButton.DANCE_PREPROGRAMMED \
               or button == ControllerButton.AUTONOME_ROUTE or button == ControllerButton.FAULT \
               or button == ControllerButton.SHUTDOWN
