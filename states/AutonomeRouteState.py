from parts.driving import DrivingHandler
from parts.vision.RouteDetector import RouteDetector



class AutonomeRouteState:
    SPEEDS_TURN_LEFT = [-4, 4]
    SPEEDS_TURN_RIGHT = [4, -4]
    SPEEDS_TURN_LEFT_WEBOTS = [-4, 4]
    SPEEDS_TURN_RIGHT_WEBOTS = [4, -4]

    def __init__(self):
        self.route_detector = RouteDetector()
        pass

    def step(self):
        """Step event for this state"""
        self._change_direction()

    def deactivate(self):
        """Function that should be run when switching away from this state"""
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
        DrivingHandler.set_speed(AutonomeRouteState.SPEEDS_TURN_LEFT[0], AutonomeRouteState.SPEEDS_TURN_LEFT[1])

    def _turn_right(self):
        """Turn the robot to the left"""
        DrivingHandler.set_speed(AutonomeRouteState.SPEEDS_TURN_RIGHT[0], AutonomeRouteState.SPEEDS_TURN_RIGHT[1])

