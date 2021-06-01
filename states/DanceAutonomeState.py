from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton


class DanceAutonomeState:
    def __init__(self):
        RemoteControl.add_listener(self)
        pass

    def step(self):
        """Step event for this state"""
        pass

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        RemoteControl.remove_listener(self)
        pass

    @staticmethod
    def get_name():
        return "Dance Autonome State"

    def on_button_press(self, button):
        """A RemoteControl listener function"""

        # Don't handle mode switches
        if ControllerButton.is_mode_button(button):
            return

    def on_sound_change(self, VU_value):
        """VU listener function"""
        # TODO: code for VU sound action
        # if VU_value == HIGH
        #     dance_command.cricle()
        # elif VU_value == MIDDLE
        #     Dance_command.up_down()
        # elif VU_value == LOW
        #     Dance_command.open_close()
