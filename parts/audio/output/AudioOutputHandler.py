from gtts import gTTS
from parts.audio.output.TextToMP3 import TextToMP3
from parts.audio.output.Speaker import Speaker


class AudioOutputHandler:
    __instance = None

    def __init__(self):
        """
            Virtually private constructor. This class is a singleton.
        """
        if AudioOutputHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioOutputHandler.__instance = self

    @staticmethod
    def get_instance():
        """
            Static access method.
        """
        if AudioOutputHandler.__instance is None:
            AudioOutputHandler()
        return AudioOutputHandler.__instance

    def speak(self, text, filename):
        """"
            Get the TextToMP3 instance and convert the given text to audio.
            Save this audio to a file with given filename
            Get the speaker and play the created file.
        """
        text_to_mp3 = TextToMP3.get_instance()
        text_to_mp3.convert(text, filename)
        speaker = Speaker.getInstance()
        speaker.play(filename + ".mp3")
