import asyncio
import time
import websockets
import threading
import json
from parts.sensors import WeightSensor
from parts.sensors import DistanceSensor
from parts.driving import DrivingHandler as drivingHandler


class WebConnection:
    __instance = None

    def __init__(self, robotController):
        """
            Virtually private constructor. This class is a singleton.
        """

        if WebConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            WebConnection.__instance = self

        self.robotController = robotController
        self.debugMessages = [] # array for debug messages

    @staticmethod
    def get_instance(robotController=None):
        """
            Static access method.
        """
        if WebConnection.__instance is None:
            WebConnection(robotController)
        return WebConnection.__instance

    def start(self):
        """
            start a websocket server on a new thread
        """
        server_host = "localhost"
        server_port = 8765  # random.randint(10000, 60000)
        new_loop = asyncio.new_event_loop()
        start_server = websockets.serve(self.send_data, server_host, server_port, loop=new_loop)
        t = threading.Thread(target=self.start_loop, args=(new_loop, start_server))
        t.start()
        print("Server launched")
        time.sleep(2)

    def start_loop(self, loop, server):
        """
            run the server until its completed and keep looping forever.
        """
        loop.run_until_complete(server)
        loop.run_forever()

    async def send_data(self, websocket, path):
        """
            Send JSON data every 2 seconds
        """
        while websocket.open:
            await websocket.send(self.get_json())
            self.remove_messages()
            await asyncio.sleep(2)

    def get_json(self):
        """
            return a json object with all sensor and actuator data
        """
        state = {
            "telemetry": {
                "sensors": {
                    "distanceSensor": DistanceSensor.get_distance(),
                    "weightSensor": WeightSensor.get_weight()
                },
                "actuators": {
                    "leftMotor": drivingHandler._left_motor.getSpeed(),
                    "rightMotor": drivingHandler._right_motor.getSpeed(),
                    "arm": "",
                    "gripper": "",
                    "leds": "led1: on, led2: off",
                    "display": ""
                },
                "remoteController": {
                    "lastPressed": "",
                    "leftJoystick": "",
                    "rightJoystick": ""
                },
                "general": {
                    "battery": "UNKNOWN",
                    "state": self.robotController.state.get_name()
                },
                "bingo": {
                    "state": "",
                    "numbers": ""
                }
            },
            "debug": self.debugMessages

        }
        return json.dumps(state)

    def add_debug_message(self, message):
        """
            add a debug message
        """
        self.debugMessages.append(message)

    def remove_messages(self):
        """
            remove debug message
        """
        self.debugMessages.clear()
