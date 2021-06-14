from parts.remote.RemoteControlListener import RemoteControlListener


class TestListener(RemoteControlListener):

    def on_joystick_change(self, left_amount, right_amount):
        print("Left: " + str(left_amount) + " right: " + str(right_amount))

    def on_button_press(self, button):
        print("Button: " + button)

