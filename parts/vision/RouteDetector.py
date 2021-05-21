class RouteDetector:
    LEFT = "left"
    RIGHT = "right"
    FRONT = "front"

    def __init__(self):
        pass

    def get_direction(self):
        """Returns the direction to go to determined through vision.
        Can return:
            RouteDetector.LEFT / "left"
            RouteDetector.RIGHT / "right"
            RouteDetector.FRONT / "front"
        """
        return RouteDetector.LEFT
