import time
from parts.MicroController import MicroController
from enum import Enum


class Mode(Enum):
    BINGO = 1
    VU = 2


selected_mode = Mode.BINGO
sending = False


def _to_base_10(low, mid, high):
    return low * pow(6, 2) + mid * pow(6, 1) + high * pow(6, 0)


def show_bingo_number_on_display(number):
    """Shows the number on the display connected to the MicroController"""
    global sending
    if sending:
        return
    if not selected_mode == Mode.BINGO:
        sending = True
        MicroController.get_instance().send_one_byte(254)
        time.sleep(0.4)
        sending = False
    MicroController.get_instance().send_one_byte(number)


def show_vu(low, mid, high):
    """Sends the data to the MicroController"""
    global sending
    if sending:
        return
    if not selected_mode == Mode.VU:
        sending = True
        MicroController.get_instance().send_one_byte(255)
        time.sleep(0.4)
        sending = False
    MicroController.get_instance().send_one_byte(_to_base_10(low, mid, high))
