from datetime import datetime


def log(message):
    """The general log function that should be used whenever anything should be logged."""
    _print_to_console(message)


def _print_to_console(message):
    """Function to be used when logging to console."""
    time = datetime.now().strftime("%H:%M:%S")
    print(time + " - " + message)


# todo: send message to website
# todo: log to file