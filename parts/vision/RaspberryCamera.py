from picamera.array import PiRGBArray
from picamera import PiCamera
from parts.vision.Camera import Camera


class RaspberryCamera(Camera):
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)

    def read_frame(self):
        RaspberryCamera.camera.capture(RaspberryCamera.rawCapture, format="bgr")
        return RaspberryCamera.rawCapture.array


