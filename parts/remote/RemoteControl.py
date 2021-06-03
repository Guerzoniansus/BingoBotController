from parts.remote.ControllerButton import ControllerButton

listeners = []

def _on_message_received(data_object):
    if data_object['mode'] == 'manual':
        __received_manual_data(data_object)

def __received_manual_data(data_object):
    for listener in listeners:
        listener.on_joystick_change(data_object['left_joy_Y'], data_object['right_joy_Y'])

        if data_object['gripper'] == 'open':
            listener.on_button_press(ControllerButton.GRIPPER_OPEN)
        elif data_object['gripper'] == 'close':
            listener.on_button_press(ControllerButton.GRIPPER_CLOSE)

        if data_object['arm'] == 'up':
            listener.on_button_press(ControllerButton.ARM_UP)
        elif data_object['arm'] == 'down':
            listener.on_button_press(ControllerButton.ARM_DOWN)

def add_listener(listener):
    """Add a RemoteControl listener to this remote controller that gets notified for controller events.
    A RemoteControl listener should have the following two public functions:
    - on_button_press(ControllerButton)
    - on_joystick_change(left_amount, right_amount)
    """
    listeners.append(listener)

def remove_listener(listener):
    """Remove a RemoteControl listener from the list of listeners."""
    listeners.remove(listener)
