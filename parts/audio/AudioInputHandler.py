import speech_recognition as sr
import threading
from parts.audio.Microphone import Microphone


class AudioInputHandler:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if AudioInputHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioInputHandler.__instance = self

        self.listeners = []
        self.isListening = False
        self.t = threading.Thread(target=self.listening)

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AudioInputHandler.__instance is None:
            AudioInputHandler()
        return AudioInputHandler.__instance

    def startListening(self):
        print("started")
        self.isListening = True
        self.t.start()

    def stopListening(self):
        self.isListening = False
        self.t.join()
        print("stopped")

    def listening(self):
        while self.isListening:
            print("listening")
            r = sr.Recognizer()
            mic = Microphone.getInstance()
            try:
                text = r.recognize_google(mic.getAudio(), language="nl-NL")
                for key_value in self.listeners:
                    if key_value["phrase"] in text.lower():
                        key_value['listener'].onHeard()
            except Exception as e:
                print('Please speak again.')

    def addListener(self, phrase, listener):
        self.listeners.append({
            "phrase": phrase,
            "listener": listener
        })
        # self.listeners[phrase] = listener
        # print(self.listeners)

    def onHeard(self):
        print("het werkt")

    def removeListener(self, listener):
        for key_value in self.listeners:
            if key_value['listener'] == listener:
                self.listeners.remove(key_value)
                return
