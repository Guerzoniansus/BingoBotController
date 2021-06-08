

class MicroController:

    __instance = None

    def __init__(self):
        """An instance will be created if none exists
        Else an exception is raised.
        The I2C connection with the MicroController is also established"""
        # TODO: needs to be implemented
        pass

    def show_on_display(self, text):
        """The microcontroller get a message to show the text in the parameters on the display
        text: String representing the text which must be shown on the display"""
        # TODO: needs to be implemented
        pass

    def get_weight(self):
        """Returns the weight of the load cell, which is connected to the microcontroller
        Return: The weight in grams"""
        # TODO: needs to be implemented
        pass

    @staticmethod
    def get_instance():
        """Returns the existing instance of the microcontroller or creates one
        Return: The new of existing MicroController instance"""
        if MicroController.__instance is None:
            MicroController.__instance = MicroController()
        return MicroController.__instance