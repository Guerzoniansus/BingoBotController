from abc import ABC, abstractmethod


class Motor(ABC):

    def __init__(self, max_speed):
        self.MAX_SPEED = max_speed
        super().__init__()

    @abstractmethod
    def set_speed(self, speed):
        pass

    def _limit_speed(self, speed):
        """ A function that makes sure speed is not above max speed or below minimum speed.
        Returns a capped speed if the speed is too big or small.
        """
        if speed > self.MAX_SPEED:
            return self.MAX_SPEED
        if speed < (self.MAX_SPEED * -1):
            return self.MAX_SPEED * -1

        return speed