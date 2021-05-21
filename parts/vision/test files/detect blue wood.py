import cv2
import numpy as np

# ====================================
# This is the file that was originally used to create the route detector.
# That means it still contains things such as preview windows and console logging.
# That also means is still has an infinite loop at the bottom, since this file was originally a standalone program.
# It can still be used for standalone testing by running it AS A STAND ALONE PROGRAM
# by changing loaded_image to blue.jpg, blue_left.jpg or blue_right.jpg as needed.
# Some useful links:
# https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html
# https://stackoverflow.com/questions/57262974/tracking-yellow-color-object-with-opencv-python
# https://stackoverflow.com/questions/48145249/how-to-get-screen-coordinates-from-color-detection-resultant-area-obtained-from
# ====================================

loaded_image = cv2.imread('blue.jpg')

LEFT = "left"
RIGHT = "right"
FORWARD = "forward"

# Minimum amount of pixels that the center x of the blue wood needs to be away from the center of the image
# before telling the robot to turn left / right
MIN_DISTANCE_FROM_CENTER = 30


def get_wood_center_x(image):
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
    contours = contours[0] if len(contours) == 2 else contours[1]  # this line is copied from stackoverflow, it had no explanation, no idea how important it is

    # No blue object found
    if len(contours) == 0:
        return -1

    # At this spot used to be code to check if it's actually a rectangle, but that got removed later.
    # See the bottom of this file for more info.

    # Largest blue thing
    largest_contour = max(contours, key=cv2.contourArea)

    wood_x, wood_y, wood_width, wood_height = cv2.boundingRect(largest_contour)
    wood_center_x = wood_x + (wood_width / 2)
    print("center x of wood = " + str(wood_center_x))

    # Draw green border around wood
    cv2.rectangle(image, (wood_x, wood_y), (wood_x + wood_width, wood_y + wood_height), (0, 255, 0), 2)

    # Check center of wood with red rectangle, casting center_x to int because otherwise errors appear
    cv2.rectangle(image, (int(wood_center_x), wood_y), (int(wood_center_x) + 2, wood_y + 30), (0, 0, 255), 2)

    # Show preview
    cv2.imshow('mask', mask)

    return wood_center_x


def get_image_center_x(image):
    """Returns the center of the given image"""

    image_height, image_width, image_channels = image.shape
    image_center_x = image_width / 2

    # Show the area in-between which the wood needs to be to return "forward"
    cv2.rectangle(image, (int(image_center_x - MIN_DISTANCE_FROM_CENTER), 0),
                  (int(image_center_x + MIN_DISTANCE_FROM_CENTER), image_height), (0, 255, 255))

    return image_center_x


def get_direction(image):
    """Returns 'left', 'right' or 'forward'.
    Returns 'right' if no blue object could be found so it can look for it.
    """

    # EXAMPLE RESULT https://i.imgur.com/e0HlJEq.png
    # Yellow rectangle = blue needs to be in-between to count as "forward"
    # Otherwise it returns left / right if the blue wood is outside of it

    wood_center_x = get_wood_center_x(image)

    if wood_center_x == -1:
        print("No blue object was found")
        return RIGHT

    image_center_x = get_image_center_x(image)

    should_turn_left = wood_center_x < (image_center_x - MIN_DISTANCE_FROM_CENTER)
    if should_turn_left:
        return LEFT

    should_turn_right = wood_center_x > (image_center_x + MIN_DISTANCE_FROM_CENTER)
    if should_turn_right:
        return RIGHT

    return FORWARD


while True:
    cv2.imshow('image', loaded_image)

    # Copying image so the original doesnt get altered
    copied_image = loaded_image.copy()

    direction = get_direction(copied_image)
    print(direction)

    # Show preview
    cv2.imshow("preview", copied_image)

    # Check if Escape is pressed to exit the program
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

# This code below was written to detect rectangles that have a similar shape to the piece of wood.
# It does so by doing width / height and comparing that ratio to the ratio of the piece of wood.
# However I realized that since the robot rotates around while staying in place, the piece of wood
# will constantly have a different ratio because you're viewing it from different angles.
# So.... useless piece of code. The code was tested and worked though.

# rectangles = []
#
# wood_ratio = 3
# wood_min_ratio = wood_ratio - 0.5
# wood_max_ratio = wood_ratio + 0.5
#
# for c in contours:
#     cx, cy, cw, ch = cv2.boundingRect(c)
#     contour_ratio = ch / cw
#     if wood_min_ratio <= contour_ratio <= wood_max_ratio:
#         rectangles.append(c)
#
# #print("ok")
#
# #To do: len(rectangles) what if there is no rectangle?
# #To do: error handling
# print("rectangles: " + str(len(rectangles)))
# largest_contour = max(rectangles, key=cv2.contourArea)
