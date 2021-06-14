from datetime import datetime

from parts.driving import DrivingHandler


class DriveMove:

    def __init__(self, speed):
        self.speed = speed

    def step(self):
        """ Set the DrivingHandler speed for the move """
        # [0] = left motor [1] = right motor
        DrivingHandler.set_speed(self.speed[0], self.speed[1])
