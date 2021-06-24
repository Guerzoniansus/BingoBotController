from parts.driving import DrivingHandler


try:
    while True:
        DrivingHandler.set_speed(20, 0)
except KeyboardInterrupt:
    DrivingHandler.set_speed(0, 0)
