from datetime import datetime
import web_connection.WebConnection
import atexit

class Logger:
    file = None
    _instance = None

    def __init__(self):
        self.file = open("log.txt", "a")
        atexit.register(self.exit_handler)

    @staticmethod
    def get_instance():
        """Creates an instance of the Gripper if there isn't one yet
        Return: the new or existing instance of the Gripper"""
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def log(self, message):
        """The general log function that should be used whenever anything should be logged."""
        formatted_message = self._format_message(message)
        self._print_to_console(formatted_message)
        self._print_to_file(formatted_message)
        self._print_to_website(formatted_message)


    def _print_to_console(self, message):
        """Function to be used when logging to console."""
        print(self, message)


    def _print_to_website(self, message):
        web_connection.WebConnection.WebConnection.get_instance().add_debug_message(message)

    def _print_to_file(self, message):
        if self.file is not None:
            self.file.write(message + "\n")

    def _format_message(self, message):
        """Formats a message into an uniform standard for debug messages.
        Right now it adds a timestamp to every message.
        """
        time = datetime.now().strftime("%H:%M:%S")
        return time + " - " + message

    def exit_handler(self):
        self.file.close()
