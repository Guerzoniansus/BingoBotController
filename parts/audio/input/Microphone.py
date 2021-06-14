import speech_recognition as sr


class Microphone:
    __instance = None

    def __init__(self):
        """
            Virtually private constructor. This class is a singleton.
        """
        if Microphone.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Microphone.__instance = self

    @staticmethod
    def get_instance():
        """
            Static access method.
        """
        if Microphone.__instance is None:
            Microphone()
        return Microphone.__instance

    def get_audio(self, source):
        """
            Returns the audio that is heard by the microphone
        """
        return sr.Recognizer().listen(source, phrase_time_limit=4)

    def get_source(self):
        with sr.Microphone() as source:
            return source
