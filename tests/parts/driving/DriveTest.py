import time

from parts.driving import DrivingHandler

while True:
    DrivingHandler.set_speed(50, 50)
    time.sleep(2)
    DrivingHandler.set_speed(-50, -50)
    time.sleep(2)
