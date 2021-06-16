import Constants
import time
import RPi.GPIO as GPIO


def get_distance():
    """Returns the distance between the robot and the object in front"""
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Constants.DISTANCE_SENSOR_TRIGGER, GPIO.OUT)
    GPIO.setup(Constants.DISTANCE_SENSOR_ECHO, GPIO.IN)

    # set the trigger to HIGH for a very short time
    GPIO.output(Constants.DISTANCE_SENSOR_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(Constants.DISTANCE_SENSOR_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(Constants.DISTANCE_SENSOR_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(Constants.DISTANCE_SENSOR_ECHO) == 1:
        stop_time = time.time()

    # Calculate the time between the stop and start time
    time_elapsed = stop_time - start_time
    # Multiply the elapsed time by 34300cm/s and divide it by 2 because the signal went to the object AND BACk
    distance = (time_elapsed * 34300) / 2

    return distance
