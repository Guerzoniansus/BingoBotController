import playsound


class Speaker:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Speaker.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Speaker.__instance = self

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Speaker.__instance is None:
            Speaker()
        return Speaker.__instance

    def play(self, file):
        playsound.playsound("media/" + file)
