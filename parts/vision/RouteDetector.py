import cv2
import numpy as np
import Constants
from parts.vision.CameraDetector import CameraDetector


class RouteDetector(CameraDetector):
    LEFT = "left"
    RIGHT = "right"
    FRONT = "front"

    # Minimum amount of pixels that the center x of the blue wood needs to be away from the center of the image
    # before telling the robot to turn left / right
    # Default is 30, it's 10 for webots
    MIN_DISTANCE_FROM_CENTER = 8

    def __init__(self):
        super().__init__()

    def _get_wood_center_x(self, image):
        """Returns the center X coordinate of the largest blue object it can find in the given image.
        Returns -1 if no blue object could be found.
        """

        # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Blue of the piece of wood
        lower_blue = np.array([95, 130, 130])
        upper_blue = np.array([110, 255, 255])

        # Filter out all blue stuff
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Get each individual blue thing
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[
            1]  # this line is copied from stackoverflow, it had no explanation, no idea how important it is

        # No blue object found
        if len(contours) == 0:
            return -1, -1

        # At this spot used to be code to check if it's actually a rectangle, but that got removed later.
        # See the bottom of the "test files/detect blue wood.py" for more info


        # NIEUWE CODE =======================
        rectangles = []

        wood_ratio = 3
        wood_min_ratio = wood_ratio - 1
        wood_max_ratio = wood_ratio + 1

        for c in contours:
            cx, cy, cw, ch = cv2.boundingRect(c)
            contour_ratio = ch / cw
            if wood_min_ratio <= contour_ratio <= wood_max_ratio:
                rectangles.append(c)

        if len(rectangles) == 0:
            return -1, -1

        #To do: error handling
        # print("rectangles: " + str(len(rectangles)))

        # Largest blue thing
        largest_contour = max(rectangles, key=cv2.contourArea)

        wood_x, wood_y, wood_width, wood_height = cv2.boundingRect(largest_contour)
        wood_center_x = wood_x + (wood_width / 2)
        wood_center_y = wood_y + (wood_height / 2)

        return wood_center_x, wood_center_y

    def _get_image_center_x(self, image):
        """Returns the center of the given image"""

        image_height, image_width, image_channels = image.shape
        image_center_x = image_width / 2

        return image_center_x

    def get_direction(self):
        """Returns the direction to go to determined through vision.
        Can return:
            -100% to -1% depending on how far LEFT the blue wood is from from the center
            1% to 100% depending on how far RIGHT the blue wood is from from the center
            RouteDetector.FRONT / "front" if the blue wood is in front of the robot
        Returns RouteDetector.RIGHT if no blue object found so it can search for it.
        """
        image = self._get_frame()
        print("I got the frame")

        # EXAMPLE RESULT https://i.imgur.com/e0HlJEq.png
        # Yellow rectangle = blue needs to be in-between to count as "forward"
        # Otherwise it returns left / right if the blue wood is outside of it

        wood_center_x, wood_center_y = self._get_wood_center_x(image)
        cv2.circle(image, (int(wood_center_x), int(wood_center_y)), 5, (0, 255, 0), 3)
        _show_image("Route frame", image)

        # If no blue object found
        if wood_center_x == -1:
            return RouteDetector.RIGHT

        image_center_x = self._get_image_center_x(image)

        image_height, image_width, image_channels = image.shape
        image_width_half = image_width / 2

        should_turn_left = wood_center_x < (image_center_x - RouteDetector.MIN_DISTANCE_FROM_CENTER)

        # Explanation of the math underneath https://i.imgur.com/qBdC8MN.png

        if should_turn_left:
            return ((image_width_half - wood_center_x) / image_width_half) * 100 * -1 - 1
            #return image_center_x - wood_center_x - 1

        should_turn_right = wood_center_x > (image_center_x + RouteDetector.MIN_DISTANCE_FROM_CENTER)

        if should_turn_right:
            return ((wood_center_x - image_width_half) / image_width_half) * 100 + 1
            #return image_center_x + wood_center_x - + 1

        return RouteDetector.FRONT

