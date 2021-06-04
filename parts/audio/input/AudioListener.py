from abc import ABC, abstractmethod


class AudioListener(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def onHeard(self):
        """when listener heard something"""
        pass
