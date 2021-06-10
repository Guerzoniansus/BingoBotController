import sys

import Constants
import WebotsRobot
from logger.Logger import Logger
from parts.remote import RemoteControl
from parts.remote.ControllerButton import ControllerButton
from parts.remote.RemoteControl import RemoteControl
from parts.remote.RemoteControlListener import RemoteControlListener
from states.AutonomeRouteState import AutonomeRouteState
from states.BingoState import BingoState
from states.DanceAutonomeState import DanceAutonomeState
from states.DancePreprogrammedState import DancePreprogrammedState
from states.IdleState import IdleState
from states.ManualState import ManualState
from web_connection.WebConnection import WebConnection
from parts.audio.output.AudioOutputHandler import AudioOutputHandler



class RobotController(RemoteControlListener):

    def __init__(self):
        Logger.get_instance().log("Setting up Robot Controller")
        RemoteControl.get_instance().add_listener(self)
        RemoteControl.start()

        self.state = ManualState()
        Logger.get_instance().log("State set to " + self.state.get_name())

        if Constants.USING_WEBOTS:
            Logger.log("Using Webots = TRUE")
            self._webots_init()

        webConnection = WebConnection.get_instance(self)
        webConnection.start()

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
            RemoteControl.start()

    def switch_state(self, new_state):
        """Make the robot switch to a new state"""
        pass
        # Logger.get_instance().log("Deactivating state: '" + self.state.get_name + "'")
        # self.state.deactivate()
        #
        # Logger.get_instance().log("Switching to new state: '" + new_state.get_name() + "'")
        # self.state = new_state

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

    def on_button_press(self, button):
        if ControllerButton.is_mode_button(button):
            new_state = self._determine_new_state(button)
            self.switch_state(new_state)

    def on_joystick_change(self, left_amount, right_amount):
        # The main robot controller doesnt handle joysticks
        pass

    def _determine_new_state(self, button):
        """Returns a new state object that corresponds to the given button,
        or None if there is no corresponding state."""
        new_state = None

        if button == ControllerButton.BINGO:
            new_state = BingoState()

        elif button == ControllerButton.MANUAL:
            new_state = ManualState()

        elif button == ControllerButton.DANCE_AUTONOME:
            new_state = DanceAutonomeState()

        elif button == ControllerButton.DANCE_PREPROGRAMMED:
            new_state = DancePreprogrammedState()

        elif button == ControllerButton.AUTONOME_ROUTE:
            new_state = AutonomeRouteState()

        return new_state





