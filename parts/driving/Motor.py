from abc import ABC, abstractmethod


class Motor(ABC):

    def __init__(self, max_speed):
        """Sets the max speed
        max_speed: Double which represents the maximum motor speed of the motor"""
        self.MAX_SPEED = max_speed
        self.current_speed = 0

    @abstractmethod
    def set_speed(self, speed):
        """Sets the speed in of the motor
        speed: Double representing the speed"""
        pass

    def _set_current_speed(self, speed):
        """Sets the current_speed variable
        speed: The new double value for the current_speed"""
        self.current_speed = speed

    def get_speed(self):
        """Returns the current speed"""
        return self.current_speed

    def _limit_speed(self, speed):
        """ A function that makes sure speed is not above max speed or below minimum speed.
        Returns a capped speed if the speed is too big or small.
        """
        if speed > self.MAX_SPEED:
            return self.MAX_SPEED
        if speed < (self.MAX_SPEED * -1):
            return self.MAX_SPEED * -1

        return speed