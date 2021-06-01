import asyncio
import time
import websockets
import threading
import json
from parts.driving import DrivingHandler as drivingHandler


class WebConnection:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if WebConnection.__instance is None:
            WebConnection()
        return WebConnection.__instance

    def __init__(self, robotController):
        """ Virtually private constructor. """
        if WebConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            WebConnection.__instance = self

        self.robotController = robotController
        self.debugMessages = []

    def start(self):
        server_host = "localhost"
        server_port = 8765  # random.randint(10000, 60000)
        new_loop = asyncio.new_event_loop()
        start_server = websockets.serve(self.sendData, server_host, server_port, loop=new_loop)
        t = threading.Thread(target=self.start_loop, args=(new_loop, start_server))
        t.start()
        print("Server launched")
        time.sleep(2)

    def start_loop(self, loop, server):
        loop.run_until_complete(server)
        loop.run_forever()

    async def sendData(self, websocket, path):
        while websocket.open:
            await websocket.send(self.getJSON())
            self.removeMessages()
            await asyncio.sleep(2)

    def getJSON(self):
        state = {
            "telemetry": {
                "sensors": {
                    "distanceSensor": "",
                    "weightSensor": ""
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

    def addDebugMessage(self, message):
        self.debugMessages.append(message)

    def removeMessages(self):
        self.debugMessages.clear()
