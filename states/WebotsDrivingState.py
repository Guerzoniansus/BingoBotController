from enum import Enum
from datetime import datetime

from parts.driving import DrivingHandler


_SECONDS_PER_ROUTE_CHANGE = 1


class _Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4


class _Navigator:
    """A helper class that determines the pre-programmed routes to take because webots has no remote controller."""
    def __init__(self):
        self.route = [_Direction.FORWARD, _Direction.BACKWARD, _Direction.LEFT,
                      _Direction.FORWARD, _Direction.RIGHT, _Direction.BACKWARD]
        self.route_index = 0

    def get_next_direction(self):
        """Returns the next Direction to drive to."""
        if self.route_index + 1 < len(self.route):
            self.route_index = self.route_index + 1
        else:
            self.route_index = 0

        return self.route[self.route_index]


class WebotsDrivingState:
    def __init__(self):
        self._time_of_last_route_change = self._get_current_time()
        self._navigator = _Navigator()

        # Which speeds to use for which motors for which directions
        # The first double is the left motor speed, the second double is the right motor speed
        self._SPEEDS = {
            _Direction.FORWARD: [7.0, 7.0],
            _Direction.BACKWARD: [-7.0, -7.0],
            _Direction.LEFT: [-4.0, 4.0],
            _Direction.RIGHT: [4.0, -4.0]
        }

    def _get_time_difference_in_seconds(self, first_time: datetime, later_time: datetime):
        """Get the current difference between two datetime objects in seconds"""
        return (later_time - first_time).total_seconds()

    def _update_time(self):
        """Update the time since last route change to the current time
        """
        self._time_of_last_route_change = self._get_current_time()

    def _get_current_time(self):
        """Get a new datetime object of the current time"""
        return datetime.now()

    # ======================= The actual "do stuff" part of this file

    def step(self):
        # Change direction every X seconds
        if (self._get_time_difference_in_seconds(self._time_of_last_route_change, self._get_current_time())
                > _SECONDS_PER_ROUTE_CHANGE):
            self._change_direction()
            self._update_time()

    def deactivate(self):
        DrivingHandler.brake()

    @staticmethod
    def get_name():
        return "Webots Driving State"

    def _change_direction(self):
        direction = self._navigator.get_next_direction()
        left_speed = self._SPEEDS[direction][0]
        right_speed = self._SPEEDS[direction][1]
        DrivingHandler.set_speed(left_speed, right_speed)

