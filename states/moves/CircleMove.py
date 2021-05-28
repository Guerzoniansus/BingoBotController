from parts.driving import DrivingHandler


class CircleMove:

    finished = False

    def __init__(self, speed):
        self.speed = speed

    def step(self):
        if not self.finished:
            """" TODO: Left/Right motor forward and Left/Right motor backward"""
            DrivingHandler.set_speed(self.speed[1], self.speed[1])
        finished = True