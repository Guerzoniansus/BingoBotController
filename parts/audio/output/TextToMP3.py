from gtts import gTTS


class TextToMP3:
    __instance = None

    def __init__(self):
        """
            Virtually private constructor. This class is a singleton.
        """
        if TextToMP3.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TextToMP3.__instance = self

    @staticmethod
    def get_instance():
        """
            Static access method.
        """
        if TextToMP3.__instance is None:
            TextToMP3()
        return TextToMP3.__instance

    def convert(self, text, filename):
        """
            Convert the given text to audio and save to given filename
        """
        tts = gTTS(text, lang='nl')
        tts.save("media/" + filename + ".mp3")
