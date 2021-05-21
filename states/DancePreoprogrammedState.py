class DancePreprogrammedState:
    def __init__(self):
        pass

    def step(self):
        """Step event for this state"""
        pass

    def deactivate(self):
        """Function that should be run when switching away from this state"""
        pass

    @staticmethod
    def get_name():
        return "Dance Preprogrammed State"