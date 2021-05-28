from parts.driving import DrivingHandler


class DriveMove:

    def __init__(self, speed):
        self.speed = speed

    def step(self):
        """" TODO: Let's move the robot a little bit left! """
        DrivingHandler.set_speed(self.speed[0], self.speed[1])
