from smbus2 import SMBus as smbus
import json



class MicroController:

    __instance = None

    def __init__(self):
        """An instance will be created if none exists
        Else an exception is raised.
        The I2C connection with the MicroController is also established"""
        self.bus = smbus(1)
        self.address = 0x08

    def show_on_display(self, text):
        """The microcontroller get a message to show the text in the parameters on the display
        text: String representing the text which must be shown on the display"""
        self.bus.write_i2c_block_data(self.address, 0, json.dumps({ "display_text": text }))

    def get_weight(self):
        """Returns the weight of the load cell, which is connected to the microcontroller
        Return: The weight in grams"""
        self.bus.write_i2c_block_data(self.address, 0, "start_meas")  # int
        raw_data = self.bus.read_i2c_block_data(self.address, 0, 16)
        return json.loads(raw_data)['weight']

    @staticmethod
    def get_instance():
        """Returns the existing instance of the microcontroller or creates one
        Return: The new of existing MicroController instance"""
        if MicroController.__instance is None:
            MicroController.__instance = MicroController()
        return MicroController.__instance