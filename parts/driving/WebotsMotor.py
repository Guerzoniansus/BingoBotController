import WebotsRobot
from logger import Logger
from parts.driving.Motor import Motor


class WebotsMotor(Motor):


    def __init__(self, motor_id):
        """ Create a Motor used in Webots.
        ID: A string used as identifier.
        """

        self.ID = motor_id

        Logger.log("Setting up driving Webots motor '" + motor_id + "'")
        motor = WebotsRobot.webots_robot.getDevice(motor_id)
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        self.MOTOR = motor

        super(6.0)

    def set_speed(self, speed):
        """Set the speed of this motor.
        Speed: A double representing the speed to set it to.
        """
        self.MOTOR.setVelocity(self._limit_speed(speed))

