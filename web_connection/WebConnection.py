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
        await websocket.send(self.getJSON())

    def getJSON(self):
        state = {
            "debugMessages": ["message 1", "message 2"],

            "telemetry": {
                "general": {
                    "connection": "no connection",
                    "battery": "UNKNOWN",
                    "state": self.robotController.state.get_name()
                },
                "sensors": {
                    "distanceSensor": "",
                    "weightSensor": ""
                },
                "actuators": {
                    "leftMotor": drivingHandler._left_motor.getSpeed(),
                    "rightMotor": "",
                    "arm": "",
                    "gripper": ""
                },
                "remoteController": {
                    "lastPressed": "",
                    "leftJoystick": "",
                    "rightJoystick": ""
                },
                "bingo": {
                    "state": "",
                    "numbers": ""
                }
            }
        }
        return json.dumps(state)
