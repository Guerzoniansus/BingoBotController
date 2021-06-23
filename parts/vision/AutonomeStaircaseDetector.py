import cv2
import numpy as np
import Constants
from parts.vision.CameraDetector import CameraDetector


class AutonomeStaircaseDetector(CameraDetector):

    def __init__(self):
        super().__init__()

