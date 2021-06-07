import Constants
import time
import RPi.GPIO as GPIO


def get_distance():
    # set Trigger to HIGH
    GPIO.output(Constants.DISTANCE_SENSOR_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(Constants.DISTANCE_SENSOR_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(Constants.DISTANCE_SENSOR_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(Constants.DISTANCE_SENSOR_ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance