import speech_recognition as sr
import threading
from parts.audio.input.Microphone import Microphone


class AudioInputHandler:
    __instance = None

    def __init__(self):
        """
            Virtually private constructor. This class is a singleton.
        """
        if AudioInputHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioInputHandler.__instance = self
        self.listeners = []  # array that holds objects of listeners an phrases
        self.isListening = False
        self.t = threading.Thread(target=self.__listening)

    @staticmethod
    def get_instance():
        """
            Static access method.
        """
        if AudioInputHandler.__instance is None:
            AudioInputHandler()
        return AudioInputHandler.__instance

    def start_listening(self):
        """
            set isListening to true and start the thread for listening
        """
        self.isListening = True
        self.t.start()

    def stop_listening(self):
        """
            set isListening to false and stop listening (stops the thread)
        """
        self.isListening = False
        self.t.join()

    def __listening(self):
        """
            Listen to the mic and create text from it.
            Checks if the text contains a phrase from the listeners array and call onHeard function of that listener
        """
        while self.isListening:
            with sr.Microphone() as source:
                r = sr.Recognizer()
                mic = Microphone.get_instance()
                try:
                    print("listening to speach")

                    r.adjust_for_ambient_noise(source, duration=1)  # naar kijken
                    text = r.recognize_google(mic.get_audio(source), language="nl-NL")

                    for key_value in self.listeners:
                        if key_value["phrase"].lower() in text.lower():
                            key_value['listener'].on_heard()

                except Exception as e:
                    print(e)
                    print('Please speak again.')

    def add_listener(self, phrase, listener):
        """
            Add new listener to the listeners array.
        """
        self.listeners.append({
            "phrase": phrase,
            "listener": listener
        })

    def removeListener(self, listener):
        for key_value in self.listeners:
            if key_value['listener'] == listener:
                self.listeners.remove(key_value)
                return
