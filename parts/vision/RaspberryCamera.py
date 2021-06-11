import Constants
from parts.vision.Camera import Camera

if Constants.USING_PI_CAMERA:

    from picamera.array import PiRGBArray
    from picamera import PiCamera

    class RaspberryCamera(Camera):
        camera = PiCamera()
        rawCapture = PiRGBArray(camera)

        def read_frame(self):
            RaspberryCamera.camera.capture(RaspberryCamera.rawCapture, format="bgr")
            return RaspberryCamera.rawCapture.array
else:
    class RaspberryCamera(Camera):
        def read_frame(self):
            raise Exception("Please enable the PI camera in Constants.py!")

