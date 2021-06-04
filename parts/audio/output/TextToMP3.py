from gtts import gTTS


class TextToMP3:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if TextToMP3.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TextToMP3.__instance = self

    @staticmethod
    def get_instance():
        """ Static access method. """
        if TextToMP3.__instance is None:
            TextToMP3()
        return TextToMP3.__instance

    def write_text_to_file(self, text, filename):
        tts = gTTS(text, lang='nl')
        tts.save("media/" + filename + ".mp3")
