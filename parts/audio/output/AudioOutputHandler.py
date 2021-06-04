from gtts import gTTS
from parts.audio.output.TextToMP3 import TextToMP3
from parts.audio.output.Speaker import Speaker


class AudioOutputHandler:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if AudioOutputHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioOutputHandler.__instance = self

    @staticmethod
    def get_instance():
        """ Static access method. """
        if AudioOutputHandler.__instance is None:
            AudioOutputHandler()
        return AudioOutputHandler.__instance

    def speak(self, text, filename):
        text_to_mp3 = TextToMP3.get_instance()
        text_to_mp3.write_text_to_file(text, filename)
        speaker = Speaker.getInstance()
        speaker.play(filename + ".mp3")
