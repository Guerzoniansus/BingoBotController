from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def step(self):
        """Step event for this state"""
        pass

    @abstractmethod
    def deactivate(self):
        """Function that should be run when switching away from this state"""
        pass

    @abstractmethod
    def get_name(self):
        """Get the name of this state."""
        return "Idle State"