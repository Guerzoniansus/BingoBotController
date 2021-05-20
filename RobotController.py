import sys

import Constants
import WebotsRobot
from logger import Logger
from states.WebotsDrivingState import WebotsDrivingState


class RobotController:
    def __init__(self):
        Logger.log("Setting up Robot Controller")

        self.state = WebotsDrivingState()
        Logger.log("State set to " + self.state.get_name())

        if Constants.USING_WEBOTS:
            Logger.log("Using Webots = TRUE")
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

    def switch_state(self, new_state):
        """Make the robot switch to a new state"""

        Logger.log("Deactivating state: '" + self.state.get_name + "'")
        self.state.deactivate()

        Logger.log("Switching to new state: '" + new_state.get_name() + "'")
        self.state = new_state

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




