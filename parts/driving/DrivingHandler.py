import Constants
if not Constants.USING_WEBOTS:
    from parts.driving.RealMotor import RealMotor
from parts.driving.WebotsMotor import WebotsMotor

LEFT_MOTOR = 0
RIGHT_MOTOR = 1

_motors = {
    LEFT_MOTOR: WebotsMotor("left wheel motor") if Constants.USING_WEBOTS else RealMotor(Constants.LEFT_FORWARD_PIN, Constants.LEFT_BACKWARD_PIN, Constants.LEFT_PWM_PIN),
    RIGHT_MOTOR: WebotsMotor("right wheel motor") if Constants.USING_WEBOTS else RealMotor(Constants.RIGHT_FORWARD_PIN, Constants.RIGHT_BACKWARD_PIN, Constants.RIGHT_PWM_PIN)
}

def set_speed(left_speed, right_speed):
    """Set the speed of the motors.
    left_speed: the speed for the left motor(s).
    right_speed: the speed for the right motor(s).
    """
    _motors[LEFT_MOTOR].set_speed(left_speed)
    _motors[RIGHT_MOTOR].set_speed(right_speed)


def get_motor_speed(motor):
    """Returns the speed of a motor
    Example call: DrivingHandler.get_motor_speed(DrivingHandler.LEFT_MOTOR)
    """
    return _motors[motor].get_speed()


def brake():
    """Sets the speed of both motors to zero."""
    _motors[LEFT_MOTOR].set_speed(0)
    _motors[RIGHT_MOTOR].set_speed(0)
