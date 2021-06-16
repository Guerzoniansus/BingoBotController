import Constants
from parts.driving import DrivingHandler
from parts.vision.RouteDetector import RouteDetector
from states.State import State


class AutonomeRouteState(State):
    # speeds[0] = left, speeds[1] = right
    SPEEDS_TURN_LEFT = [-100, 100]
    SPEEDS_TURN_RIGHT = [100, -100]
    SPEEDS_TURN_LEFT_WEBOTS = [-4, 4]
    SPEEDS_TURN_RIGHT_WEBOTS = [4, -4]

    def __init__(self):
        self.route_detector = RouteDetector()
        pass

    def step(self):
        self._change_direction()

    def deactivate(self):
        pass

    @staticmethod
    def get_name():
        return "Autonome Route Strategy State"

    # ===================== Private methods below

    def _change_direction(self):
        """Changes direction (if needed) depending on which route to take"""
        direction = self.route_detector.get_direction()
        print(direction)

        if direction == RouteDetector.LEFT:
            self._move_backward()
        elif direction == RouteDetector.RIGHT:
#            self._move_forward()
            pass
        elif direction == RouteDetector.FRONT:
            DrivingHandler.brake()
        else:
#            direction = -direction
 #           print(direction)

#            return
            if direction < 0:
                speed = -80
#                speed = -60 + ((70 / 40) * (-100 - direction))
                #right_speed = 40 - ((70 / 45) * (-100 - direction))
            else:
                speed = 80
 #               speed = 60 - ((70 / 40) * (100 - direction))
                #right_speed = -40 + ((70 / 45) * (100 - direction))
            self._move(speed)

    def _move_forward(self):
        DrivingHandler.set_speed(100, 100)

    def _move_backward(self):
        DrivingHandler.set_speed(-100, -100)

    def _move(self, speed):
        DrivingHandler.set_speed(speed, speed)

    def _turn_left(self):
        """Turn the robot to the left"""
        speeds = [AutonomeRouteState.SPEEDS_TURN_LEFT_WEBOTS[0], AutonomeRouteState.SPEEDS_TURN_LEFT_WEBOTS[1]] if Constants.USING_WEBOTS \
            else [AutonomeRouteState.SPEEDS_TURN_LEFT[0], AutonomeRouteState.SPEEDS_TURN_LEFT[1]]

        DrivingHandler.set_speed(speeds[0], speeds[1])

    def _turn_right(self):
        """Turn the robot to the right"""
        speeds = [AutonomeRouteState.SPEEDS_TURN_RIGHT_WEBOTS[0],
                  AutonomeRouteState.SPEEDS_TURN_RIGHT_WEBOTS[1]] if Constants.USING_WEBOTS \
            else [AutonomeRouteState.SPEEDS_TURN_RIGHT[0], AutonomeRouteState.SPEEDS_TURN_RIGHT[1]]

        DrivingHandler.set_speed(speeds[0], speeds[1])
