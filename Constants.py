USING_WEBOTS = True
"""Boolean that described whether or not the program is being run on Webots.
If false, it means the real robot is being used."""

LEFT_FORWARD_PIN = 26
LEFT_BACKWARD_PIN = 20
LEFT_PWM_PIN = 12

RIGHT_FORWARD_PIN = 19
RIGHT_BACKWARD_PIN = 16
RIGHT_PWM_PIN = 13

GRIPPER_ID = 22

DISTANCE_SENSOR_TRIGGER = 6
DISTANCE_SENSOR_ECHO = 5

AX12_PORT = '/dev/ttyAMA0'
AX12_BAUDRATE = 1000000
AX12_TIMEOUT = 3.0
"""These constants are the pin-out and configuration of some parts"""

REMOTE_PORT = 9010
RPI_IP = '192.168.137.242'
