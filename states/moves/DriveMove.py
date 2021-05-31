from datetime import datetime

from parts.driving import DrivingHandler


class DriveMove:

    def __init__(self, speed):
        self.speed = speed

    def step(self):
        """" TODO: Let's move the robot a little bit left! """
        # [0] = left motor [1] = right motor
        # print("Calling the step function of the DriveMove")
        DrivingHandler.set_speed(self.speed[0], self.speed[1])
