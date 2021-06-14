import Constants
from parts.driving import DrivingHandler
from parts.vision.RouteDetector import RouteDetector
from states.State import State


class AutonomeRouteState(State):
    # speeds[0] = left, speeds[1] = right
    SPEEDS_TURN_LEFT = [-4, 4]
    SPEEDS_TURN_RIGHT = [4, -4]
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

        if direction == RouteDetector.LEFT:
            self._turn_left()
        elif direction == RouteDetector.RIGHT:
            self._turn_right()
        elif direction == RouteDetector.FRONT:
            DrivingHandler.brake()

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