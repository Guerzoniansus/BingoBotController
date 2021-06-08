import playsound


class Speaker:
    __instance = None

    def __init__(self):
        """
            Virtually private constructor. This class is a singleton.
        """
        if Speaker.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Speaker.__instance = self

    @staticmethod
    def getInstance():
        """
            Static access method.
        """
        if Speaker.__instance is None:
            Speaker()
        return Speaker.__instance

    def play(self, filename):
        """
            play the sound from the given filename
        """
        playsound.playsound("media/" + filename)
