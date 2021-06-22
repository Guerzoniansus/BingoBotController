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

        # def frame2base64(self, frame):
        #     Img = Image.fromarray(frame)
        #     Output_buffer = BytesIO()
        #     Img.save(Output_buffer, format='JPEG')
        #     Byte_data = Output_buffer.getvalue()
        #     Base64_data = base64.b64encode(Byte_data)
        #     return Base64_data
        #
        # def test_get_base64_image(self):
        #     self.camera = cv2.VideoCapture(0)
        #     try:
        #         ret, frame = camera.read()
        #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #         cv2.imshow("camera", frame)
        #         base64_data = self.frame2base64(gray).__str__()
        #         base64_data = base64_data.replace("b'", "")
        #         base64_data = base64_data.replace("'", "")
        #         return base64_data
        #     except Exception as e:
        #         print(e)

        def get_base64_image(self):
            import base64
            import io
            stream = io.BytesIO()
            with PiCamera.PiCamera() as cam:
            #     cam.rotation = _rotation
            #     cam.resolution = self._resolution
            #     if self._label:
            #         cam.annotate_text = self._label
            #     cam.start_preview()
            #     if self._rescale:
            #         cam.capture(stream, format="jpeg", resize=self._rescale, use_video_port=True)
            #     else:
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

        def get_instance(self):
            raise Exception("This camera doesn't exists!")
