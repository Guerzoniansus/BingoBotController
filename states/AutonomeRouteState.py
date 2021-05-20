from parts.driving import DrivingHandler

class AutonomeRouteState:
    SPEEDS_TURN_LEFT = [-4, 4]
    SPEEDS_TURN_RIGHT = [4, -4]
    SPEEDS_TURN_LEFT_WEBOTS = [-4, 4]
    SPEEDS_TURN_RIGHT_WEBOTS = [4, -4]

    def __init__(self):
        pass

    def step(self):
        """Step event for this state"""
        pass

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        pass

    @staticmethod
    def get_name():
        return "Autonome Route Strategy State"
