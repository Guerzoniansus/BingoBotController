import cv2
import numpy as np
import WebotsRobot
from parts.vision.Camera import Camera


class WebotsCamera(Camera):
    # Initialize camera
    camera = WebotsRobot.webots_robot.getDevice('camera')
    timestep = int(WebotsRobot.webots_robot.getBasicTimeStep())
    camera.enable(timestep)

    def read_frame():
        # Take an image from the camera device and prepare it for OpenCV processing:
        # - convert data type,
        # - convert to BGR format (from BGRA), and
        # - rotate & flip to match the actual image.
        # Code copied from Code copied from https://github.com/lukicdarkoo/webots-example-visual-tracking/blob/master/controllers/visual_tracker/visual_tracker.py

        img = WebotsCamera.camera.getImageArray()

        img = np.asarray(img, dtype=np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        img = cv2.flip(img, 1)
        return img




