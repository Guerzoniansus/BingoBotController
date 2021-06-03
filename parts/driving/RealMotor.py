from parts.driving.Motor import Motor
import RPi.GPIO as GPIO


class RealMotor(Motor):

    def __init__(self, forward_pin, backward_pin, pwm_pin):
        super(100)

        GPIO.setup(forward_pin, GPIO.OUT)
        GPIO.setup(backward_pin, GPIO.OUT)
        GPIO.setup(pwm_pin, GPIO.OUT)

        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.pwm = GPIO.PWM(pwm_pin, 100)
        self.pwm.start(0)

    def set_speed(self, value):
        GPIO.output(self.forward_pin, value >= 0)
        GPIO.output(self.backward_pin, value < 0)

        self.pwm.ChangeDutyCycle(self._limit_speed(abs(value)))

    def __del__(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
