import threading

import Constants
from parts.remote.ControllerButton import ControllerButton
import socket
import json

class RemoteControl:

    __listeners = []
    __thread = None
    __buffer_size = 1024
    __local_ip = Constants.RPI_IP
    __local_port = Constants.REMOTE_PORT
    __udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    __running = False
    __instance = None

    def __init__(self):
        """Creates a instance of the RemoteController if none exists
        Else an exception is raised"""
        if RemoteControl.__instance is not None:
            raise Exception('This class is a singleton!')

        self.__udpServerSocket.bind((self.__local_ip, self.__local_port))
        self.__running = True

    def __on_message_received(self, data_object):
        """Is called when new data is received from the remote controller
        data_object: The parse JSON data"""
        # If the mode is manual the manual data will be send
        if data_object['mode'] == 'manual':
            self.__received_manual_data(data_object)
        # Always will be sent in which mode the robot is in
        self.__send_mode(data_object)

    def __received_manual_data(self, data_object):
        """Is called when data of the manual mode is received
        All listeners will be informed with the information
        data_object: All the data from the request"""
        for listener in self.__listeners:
            listener.on_joystick_change(int(data_object['left_joy']), int(data_object['right_joy']))

            if data_object['gripper'].lower() == 'open':
                listener.on_button_press(ControllerButton.GRIPPER_OPEN)
            elif data_object['gripper'].lower() == 'close':
                listener.on_button_press(ControllerButton.GRIPPER_CLOSE)

            if data_object['arm'].lower() == 'up':
                listener.on_button_press(ControllerButton.ARM_UP)
            elif data_object['arm'].lower() == 'down':
                listener.on_button_press(ControllerButton.ARM_DOWN)

    def __send_mode(self, data_object):
        """Sends the mode to all the different listeners"""
        button = None
        if data_object['mode'] == 'bingo':
            button = ControllerButton.BINGO
        elif data_object['mode'] == 'manual':
            button = ControllerButton.MANUAL
        elif data_object['mode'] == 'dance_preprogrammed':
            button = ControllerButton.DANCE_PREPROGRAMMED
        elif data_object['mode'] == 'dance_autonome':
            button = ControllerButton.DANCE_AUTONOME
        elif data_object['mode'] == 'autonome_route':
            button = ControllerButton.AUTONOME_ROUTE
        elif data_object['mode'] == 'fault':
            button = ControllerButton.FAULT
        elif data_object['mode'] == 'shutdown':
            button = ControllerButton.SHUTDOWN

        for listener in self.__listeners:
            if button is not None:
                listener.on_button_press(button)

    def add_listener(self, listener):
        """Add a RemoteControl listener to this remote controller that gets notified for controller events.
        A RemoteControl listener should have the following two public functions:
        - on_button_press(ControllerButton)
        - on_joystick_change(left_amount, right_amount)
        """
        self.__listeners.append(listener)

    def remove_listener(self, listener):
        """Remove a RemoteControl listener from the list of listeners."""
        self.__listeners.remove(listener)

    def __run(self):
        """Is run when listening to the remote controller"""
        while self.__running:
            bytes_address_pair = self.__udpServerSocket.recvfrom(self.__buffer_size)
            message = bytes_address_pair[0].decode("utf-8")
            self.__on_message_received(json.loads(message))

    def start(self):
        """Starts the RemoteController"""
        self.__running = True
        self.__thread = threading.Thread(target=self.__run)
        self.__thread.start()

    def stop(self):
        """Stops the RemoteController"""
        self.__running = False
        if self.__thread is not None:
            if self.__thread.is_alive():
                self.__thread.join()
        self.__thread = None

    def __del__(self):
        self.stop()

    @staticmethod
    def get_instance():
        """Returns a instance if the RemoteController
        The existing one or a new one will be created
        Return: the new or existing instance"""
        if RemoteControl.__instance is None:
            RemoteControl.__instance = RemoteControl()
        return RemoteControl.__instance
