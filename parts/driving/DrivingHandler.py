import Constants
if not Constants.USING_WEBOTS:
    from parts.driving.RealMotor import RealMotor
from parts.driving.WebotsMotor import WebotsMotor

left_forward_pin = -1
left_backward_pin = -1
left_pwm_pin = -1

right_forward_pin = -1
right_backward_pin = -1
right_pwm_pin = -1

# TODO: change real motor classes to accept constructor input
_left_motor = WebotsMotor("left wheel motor") if Constants.USING_WEBOTS else RealMotor(left_forward_pin, left_backward_pin, left_pwm_pin)
_right_motor = WebotsMotor("right wheel motor") if Constants.USING_WEBOTS else RealMotor(right_forward_pin, right_backward_pin, right_pwm_pin)


def set_speed(left_speed, right_speed):
    """Set the speed of the motors.
    left_speed: the speed for the left motor(s).
    right_speed: the speed for the right motor(s).
    """

    _left_motor.set_speed(left_speed)
    _right_motor.set_speed(right_speed)



def brake():
    """Sets the speed of both motors to zero."""
    _left_motor.set_speed(0)
    _right_motor.set_speed(0)

