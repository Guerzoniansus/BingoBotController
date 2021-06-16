from parts.driving.Motor import Motor
import RPi.GPIO as GPIO


class RealMotor(Motor):

    def __init__(self, forward_pin, backward_pin, pwm_pin):
        """Sets the right GPIO pins as OUTPUT's and initializes the PWM pin
        forward_pin: The GPIO pin which needs to be HIGH to let the motor run forward
        backward_pin: The GPIO pin which needs to be HIGH to let the motor run backward
        pwm_pin: The GPIO pin where the PWM signals are going to be send to"""
        super().__init__(100)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(forward_pin, GPIO.OUT)
        GPIO.setup(backward_pin, GPIO.OUT)
        GPIO.setup(pwm_pin, GPIO.OUT)

        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.pwm = GPIO.PWM(pwm_pin, 100)
        self.pwm.start(0)

    def set_speed(self, value):
        """Set the turning speed of the motor
        value: A double value representing the speed"""
        super()._set_current_speed(value)
        GPIO.output(self.forward_pin, value >= 0)
        GPIO.output(self.backward_pin, value < 0)

        self.pwm.ChangeDutyCycle(self._limit_speed(abs(value)))

    def __del__(self):
        """Sets the PWM duty cycle to 0 to make sure the motor stopped running"""
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.forward_pin, False)
        GPIO.output(self.backward_pin, False)
        self.pwm.stop()
