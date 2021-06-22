import Constants
from parts.Ax12 import Ax12


class Gripper:

    __instance = None

    def __init__(self):
        """Creates the Gripper object of there isn't an instance of it yet
        Else an exception is raised"""
        if Gripper.__instance is not None:
            raise Exception('Gripper is a singleton!')

        self.servos = Ax12.get_instance()
        self.close_position = 0
        self.open_position = 300

        self.is_closed = False
        self.close_gripper()

    def get_is_closed(self):
        """Return the is_closed variable
        Return: true if the gripper is closed"""
        return self.is_closed

    def close_gripper(self):
        """Closes the gripper"""
        self.__move_gripper(self.close_position)

    def open_gripper(self):
        """Opens the gripper"""
        self.__move_gripper(self.open_position)

    def __move_gripper(self, position):
        """Moves the gripper in the right direction"""
        self.servos.move(Constants.GRIPPER_ID, position)

    @staticmethod
    def get_instance():
        """Creates an instance of the Gripper if there isn't one yet
        Return: the new or existing instance of the Gripper"""
        if Gripper.__instance is None:
            Gripper.__instance = Gripper()
        return Gripper.__instance