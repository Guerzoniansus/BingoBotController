from parts.Ax12 import Ax12
import time

def create_servo_object(id, down_value, up_value):
    return {
            "id": id,
            "down_value": down_value,
            "up_value": up_value
           }

class Arm:

    servo_data = [
        create_servo_object(21, 578, 822),  # 523, 826    673
        create_servo_object(18, 580, 825),  # 528, 818    678
        create_servo_object(7, 450, 199),  # 500, 203    350
        create_servo_object(1, 465, 213)  # 506, 207    356
    ]
    __instance = None

    def __init__(self):
        """"Creates an instance of the arm
        It also checks if an instance already exists.
        if so raise an exception because this class is a singleton!
        """
        if Arm.__instance is not None:
            raise Exception('This class is a singleton!')
        self.servos = Ax12.get_instance()
        self.__is_up = False
        self.arm_down()

    def is_up(self):
        """Returns true if the arm is up"""
        return self.__is_up

    def arm_up(self):
        """Moves the whole arm up"""
        if not self.is_up():
            self.__is_up = True
            self.__move_arm('up_value')

    def arm_down(self):
        """Moves the whole arm down"""
        if self.is_up():
            self.__is_up = False
            self.__move_arm('down_value')


    def __move_arm(self, value_name):
        # Iterate through all servos and set them to the position corresponding by the value_name
        for servo in self.servo_data:
            self.servos.moveSpeed(servo['id'], servo[value_name], 200)
            time.sleep(0.01)

    @staticmethod
    def get_instance():
        """Returns the instance of the Arm
        If it doesn't exist yet it will be created"""
        if Arm.__instance is None:
            Arm.__instance = Arm()
        return Arm.__instance