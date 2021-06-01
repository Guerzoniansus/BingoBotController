from abc import ABC, abstractmethod

class RemoteControlListener(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_joystick_change(self, left_amount, right_amount):
        """Event that gets fired when the joysticks get moved."""
        pass

    @abstractmethod
    def on_button_press(self, button):
        """Event that gets fired when a button is pressed on the remote controller."""
        pass
