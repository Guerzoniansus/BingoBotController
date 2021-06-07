webots_robot = None

try:
    from controller import Robot
except:
    pass
else:
    webots_robot = Robot()


