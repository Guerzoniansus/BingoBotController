import Constants
from parts.Ax12 import Ax12


class Gripper:

    __instance = None

    def __init__(self):
        if Gripper.__instance is not None:
            raise Exception('Gripper is a singleton!')

        self.servos = Ax12.get_instance()
        self.close_position = 0
        self.open_position = 300

        self.is_closed = False
        self.close_gripper()

    def get_position(self):


    def close_gripper(self):
        self.__move_gripper(self.close_position)

    def open_gripper(self):
        self.__move_gripper(self.open_position)

    def __move_gripper(self, position):
        self.servos.move(Constants.gripper_id, position)

    @staticmethod
    def get_instance():
        if Gripper.__instance is None:
            Gripper.__instance = Gripper()
        return Gripper.__instance