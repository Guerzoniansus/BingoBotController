from parts.MicroController import MicroController


def _to_base_10(low, mid, high):
    return low * pow(6, 2) + mid * pow(6, 1) + high * pow(6, 0)


def show_bingo_number_on_display(number):
    """Shows the number on the display connected to the MicroController"""
    MicroController.get_instance().send_one_byte(number)


def show_vu(low, mid, high):
    """Sends the data to the MicroController"""
    MicroController.get_instance().send_one_byte(_to_base_10(low, mid, high))
