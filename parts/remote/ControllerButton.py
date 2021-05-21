from enum import Enum


class ControllerButton(Enum):
    BINGO = 1
    MANUAL = 2
    DANCE_AUTONOME = 3
    DANCE_PREPROGRAMMED = 4
    AUTONOME_ROUTE = 5
    ARM_UP = 6
    ARM_DOWN = 7
    GRIPPER_OPEN = 8
    GRIPPER_CLOSE = 9

    def is_mode_button(button):
        """Returns true if the button is a switch mode button."""
        return button == ControllerButton.BINGO or button == ControllerButton.MANUAL \
               or button == ControllerButton.DANCE_AUTONOME or button == ControllerButton.DANCE_PREPROGRAMMED \
               or button == ControllerButton.AUTONOME_ROUTE
