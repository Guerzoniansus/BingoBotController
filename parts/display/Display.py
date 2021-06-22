from parts.MicroController import MicroController


def show_bingo_number_on_display(number):
    """Shows the number on the display connected to the MicroController"""
    MicroController.get_instance().show_bingo_number_on_display(number)


def show_vu(low, mid, high):
    """Sends the data to the MicroController"""
    pass
