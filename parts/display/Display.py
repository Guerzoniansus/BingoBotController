from parts.MicroController import MicroController


def show_on_display(text):
    """Shows text on the display connected to the MicroController"""
    MicroController.get_instance().show_on_display(text)