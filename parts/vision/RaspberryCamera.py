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

        def get_base64_image(self):
            import base64
            import io
            stream = io.BytesIO()
            with picamera.PiCamera() as cam:
                cam.rotation = self._rotation
                cam.resolution = self._resolution
                if self._label:
                    cam.annotate_text = self._label
                cam.start_preview()
                if self._rescale:
                    cam.capture(stream, format="jpeg", resize=self._rescale, use_video_port=True)
                else:
                    cam.capture(stream, format="jpeg", use_video_port=True)
            stream.seek(0)
            return self.__parse(base64.b64encode(stream.read()))

        def __parse(self, base64_encoded_string):
            result = base64_encoded_string.replace("b'", "")
            result = result.replace("'", "")
            return result
else:
    class RaspberryCamera(Camera):
        def read_frame(self):
            raise Exception("Please enable the PI camera in Constants.py!")
