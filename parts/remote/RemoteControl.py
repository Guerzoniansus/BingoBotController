listeners = []

def _on_message_received(message):
    pass
    # EXAMPLE CODE: GRIPER_OPEN was pressed:
    # for listener in listeners:
        # listener.on_button_press(ControllerButton.GRIPPER_OPEN)

    # EXAMPLE CODE: joysticks were pushed
    # Pretend these amounts were gotten from the joystick
    # for listener in listeners:
        # listener.on_joystick_change(left_amount, right_amount)


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
