from abc import ABC, abstractmethod


class AudioListener(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def onHeard(self):
        """
            Function that is called when the listener heard something
        """
        pass
