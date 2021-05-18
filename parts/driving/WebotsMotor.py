import WebotsRobot
from logger import Logger


class WebotsMotor:

    def __init__(self, ID):
        """ Create a Motor used in Webots.
        ID: A string used as identifier.
        """

        self.ID = ID

        Logger.log("Setting up driving motor '" + ID + "'")
        motor = WebotsRobot.webots_robot.getDevice(ID)
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        self.MOTOR = motor
        self.MAX_SPEED = 6.0

    def set_speed(self, speed):
        """Set the speed of this motor.
        Speed: A double representing the speed to set it to.
        """
        self.MOTOR.setVelocity(self._limit_speed(speed))

    def _limit_speed(self, speed):
        """ A function that makes sure speed is not above max speed or below minimum speed.
        Returns a capped speed if the speed is too big or small.
        """
        if speed > self.MAX_SPEED:
            return self.MAX_SPEED
        if speed < (self.MAX_SPEED * -1):
            return self.MAX_SPEED * -1

        return speed
