from smbus2 import SMBus as smbus
import json



class MicroController:

    __instance = None

    def __init__(self):
        """An instance will be created if none exists
        Else an exception is raised.
        The I2C connection with the MicroController is also established"""
        if MicroController.__instance is not None:
            raise Exception("This class is a singleton!")

        self.bus = smbus(1)
        self.address = 0x08

    def show_bingo_number_on_display(self, number):
        """The microcontroller gets a number in the parameters to show on the display
        number: Integer representing the number which must be shown on the display"""
        self.bus.write_byte_data(self.address, 0, number)

    def get_weight(self):
        """Returns the weight of the load cell, which is connected to the microcontroller
        Return: The weight in grams"""
        data = self.bus.read_i2c_block_data(self.address, 0, 6)
        a = ''.join(chr(x) for x in data)
        return float(a) - 8

    @staticmethod
    def get_instance():
        """Returns the existing instance of the microcontroller or creates one
        Return: The new of existing MicroController instance"""
        if MicroController.__instance is None:
            MicroController.__instance = MicroController()
        return MicroController.__instance
