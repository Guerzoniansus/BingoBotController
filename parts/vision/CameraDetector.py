from abc import ABC

import Constants
import cv2
if not Constants.USING_WEBOTS:
    from parts.vision.RaspberryCamera import RaspberryCamera
else:
    from parts.vision.WebotsCamera import WebotsCamera


class CameraDetector(ABC):

    def __init__(self):
        self.__camera_instance = RaspberryCamera.get_instance() if not Constants.USING_WEBOTS else WebotsCamera

    def _show_image(self, window_name, frame):
        if Constants.SHOW_VIDEO_STREAM:
            cv2.imshow(window_name, frame)
            cv2.waitKey(1)

    def _get_frame(self):
        """Get an image frame from the camera."""
        return self.__camera_instance.read_frame()
