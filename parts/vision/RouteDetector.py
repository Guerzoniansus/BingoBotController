import cv2
import numpy as np
import Constants
if not Constants.USING_WEBOTS:
    from parts.vision.RaspberryCamera import RaspberryCamera

try:
    from parts.vision.WebotsCamera import WebotsCamera
except:
    pass


class RouteDetector:
    LEFT = "left"
    RIGHT = "right"
    FRONT = "front"

    # Minimum amount of pixels that the center x of the blue wood needs to be away from the center of the image
    # before telling the robot to turn left / right
    # Default is 30, it's smaller for webots
    MIN_DISTANCE_FROM_CENTER = 10

    def __init__(self):
        pass

    def _get_wood_center_x(self, image):
        """Returns the center X coordinate of the largest blue object it can find in the given image.
        Returns -1 if no blue object could be found.
        """

        # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Blue of the piece of wood
        lower_blue = np.array([95, 100, 50])
        upper_blue = np.array([110, 255, 255])

        # Filter out all blue stuff
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Get each individual blue thing
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[
            1]  # this line is copied from stackoverflow, it had no explanation, no idea how important it is

        # No blue object found
        if len(contours) == 0:
            return -1

        # At this spot used to be code to check if it's actually a rectangle, but that got removed later.
        # See the bottom of the "test files/detect blue wood.py" for more info

        # Largest blue thing
        largest_contour = max(contours, key=cv2.contourArea)

        wood_x, wood_y, wood_width, wood_height = cv2.boundingRect(largest_contour)
        wood_center_x = wood_x + (wood_width / 2)

        return wood_center_x

    def _get_image_center_x(self, image):
        """Returns the center of the given image"""

        image_height, image_width, image_channels = image.shape
        image_center_x = image_width / 2

        return image_center_x

    def get_direction(self):
        """Returns the direction to go to determined through vision.
        Can return:
            RouteDetector.LEFT / "left"
            RouteDetector.RIGHT / "right"
            RouteDetector.FRONT / "front"
        Returns RIGHT if no blue object found so it can search for it.
        """

        image = self._get_frame()

        cv2.imshow("img", image)

        # EXAMPLE RESULT https://i.imgur.com/e0HlJEq.png
        # Yellow rectangle = blue needs to be in-between to count as "forward"
        # Otherwise it returns left / right if the blue wood is outside of it

        wood_center_x = self._get_wood_center_x(image)

        # If no blue object found
        if wood_center_x == -1:
            return RouteDetector.RIGHT

        image_center_x = self._get_image_center_x(image)

        should_turn_left = wood_center_x < (image_center_x - RouteDetector.MIN_DISTANCE_FROM_CENTER)
        if should_turn_left:
            return RouteDetector.LEFT

        should_turn_right = wood_center_x > (image_center_x + RouteDetector.MIN_DISTANCE_FROM_CENTER)
        if should_turn_right:
            return RouteDetector.RIGHT

        return RouteDetector.FRONT

    def _get_frame(self):
        """Get an image frame from the camera."""
        return RaspberryCamera.get_instance().read_frame() if not Constants.USING_WEBOTS else WebotsCamera.read_frame()
