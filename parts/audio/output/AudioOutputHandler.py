from gtts import gTTS


class AudioOutputHandler:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if AudioOutputHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioOutputHandler.__instance = self

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AudioOutputHandler.__instance is None:
            AudioOutputHandler()
        return AudioOutputHandler.__instance

    def createAudioFromText(self, text, filename):
        tts = gTTS(text, lang='nl')
        tts.save("media/" + filename + ".mp3")
