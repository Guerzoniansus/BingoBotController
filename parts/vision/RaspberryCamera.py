from picamera.array import PiRGBArray
from picamera import PiCamera


camera = PiCamera()
rawCapture = PiRGBArray(camera)


def read_frame():
    """Returns an image frame from the Raspberry PI camera in OpenCV type."""
    camera.capture(rawCapture, format="bgr")
    return rawCapture.array
