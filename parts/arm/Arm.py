from parts.Ax12 import Ax12
import time

def create_servo_object(id_, down_value, up_value):
    return {
            "id": id_,
            "down_value": down_value,
            "up_value": up_value
        }



class Arm:

    servo_data = [
        create_servo_object(21, 573, 826),  # 523, 826    673
        create_servo_object(18, 578, 818),  # 528, 818    678
        create_servo_object(7, 450, 203),   # 500, 203    350
        create_servo_object(1, 456, 207)    # 506, 207    356
    ]
    __instance = None

    def __init__(self):
        if Arm.__instance is not None:
            raise Exception('This class is a singleton!')
        self.servos = Ax12.get_instance()
        self.__is_up = False
        self.arm_down()

    def is_up(self):
        return self.__is_up

    def arm_up(self):
        self.__is_up = True
        for servo in self.servo_data:
            self.servos.moveSpeed(servo['id'], servo['up_value'], 300)
            time.sleep(0.01)

    def arm_down(self):
        self.__is_up = False
        for servo in self.servo_data:
            self.servos.moveSpeed(servo['id'], servo['down_value'], 200)
            time.sleep(0.01)

    @staticmethod
    def get_instance():
        if Arm.__instance is None:
            Arm.__instance = Arm()
        return Arm.__instance