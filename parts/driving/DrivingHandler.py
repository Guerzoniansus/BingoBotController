import Constants
from parts.driving.RealMotor import RealMotor
from parts.driving.WebotsMotor import WebotsMotor

# TODO: change real motor classes to accept constructor input
_left_motor = WebotsMotor("left wheel motor") if Constants.USING_WEBOTS else RealMotor()
_right_motor = WebotsMotor("right wheel motor") if Constants.USING_WEBOTS else RealMotor()


def set_speed(left_speed, right_speed):
    """Set the speed of the motors.
    left_speed: the speed for the left motor(s).
    right_speed: the speed for the right motor(s).
    """

    _left_motor.set_speed(left_speed)
    _right_motor.set_speed(right_speed)
