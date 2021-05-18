import sys

import Constants
import WebotsRobot
from controller import Robot
from states.WebotsDrivingState import WebotsDrivingState


class RobotController:
    def __init__(self):

        self.state = WebotsDrivingState()

        if Constants.USING_WEBOTS:
            self._webots_init()

    # ==================================================================
    #               _           _
    # __      _____| |__   ___ | |_ ___
    # \ \ /\ / / _ \ '_ \ / _ \| __/ __|
    #  \ V  V /  __/ |_) | (_) | |_\__ \
    #   \_/\_/ \___|_.__/ \___/ \__|___/
    def _webots_init(self):
        self.WEBOTS_TIME_STEP = int(WebotsRobot.webots_robot.getBasicTimeStep())

    # ==================================================================

    def start(self):
        """Start the robot"""
        if Constants.USING_WEBOTS:
            self._do_webots_loop()

        else:
            self._do_normal_loop()

    def _do_normal_loop(self):
        """A normal main loop thats repeats infinitely"""
        while True:
            self._step()

    def _do_webots_loop(self):
        """A version of the main loop that is used in webots"""
        while WebotsRobot.webots_robot.step(self.WEBOTS_TIME_STEP) != -1:
            self._step()

    def _step(self):
        """The main step event of the robot controller that gets executed every loop"""
        self.state.step()
        return

    def shutdown(self):
        """A function used for safely shutting down the robot program"""
        sys.exit(0)




