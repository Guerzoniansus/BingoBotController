import threading

from parts.remote.ControllerButton import ControllerButton
import socket
import json

listeners = []
__thread = threading.Thread(target=__file__.__run)
__buffer_size = 1024
__local_ip = '141.252.29.9'
__local_port = '9010'
__udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
__running = False


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

def __run():
    while __running:
        bytes_address_pair = __udpServerSocket.recvfrom(__buffer_size)
        message = bytes_address_pair[0].decode("utf-8")
        _on_message_received(json.loads(message))

def start():
    __udpServerSocket.bind((__local_ip, __local_port))
    __file__.__running = True

def stop():
    __file__.__running = False
    __thread.join()