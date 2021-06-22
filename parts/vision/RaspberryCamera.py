import base64
from io import BytesIO
from PIL import Image

import Constants
from parts.vision.Camera import Camera

if Constants.USING_PI_CAMERA:

    from picamera.array import PiRGBArray
    from picamera import PiCamera


    class RaspberryCamera(Camera):

        __instance = None

        def __init__(self):
            if RaspberryCamera.__instance is not None:
                raise Exception("RobotController is a Singleton!")

            RaspberryCamera.__instance = self

            self.camera = PiCamera()
            self.raw_capture = PiRGBArray(self.camera)

        @staticmethod
        def get_instance():
            if RaspberryCamera.__instance is None:
                RaspberryCamera()
            return RaspberryCamera.__instance

        def read_frame(self):
            self.__instance.camera.capture(self.raw_capture, format="bgr")
            image = self.raw_capture.array
            self.raw_capture.truncate(0)
            return image

        def get_base64_image(self):
            self.frame2base64(self.read_frame())

        def frame2base64(self, frame):
            Img = Image.fromarray(frame)
            Output_buffer = BytesIO()
            Img.save(Output_buffer, format='JPEG')
            Byte_data = Output_buffer.getvalue()
            Base64_data = base64.b64encode(Byte_data)
            return self.__parse(Base64_data)

        def __parse(self, base64_encoded_string):
            result = base64_encoded_string.replace("b'", "")
            result = result.replace("'", "")
            return result
else:

    class RaspberryCamera(Camera):

        def read_frame(self):
            raise Exception("Please enable the PI camera in Constants.py!")

        def get_instance(self):
            raise Exception("This camera doesn't exists!")
