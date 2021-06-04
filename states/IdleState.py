from states.State import State


class IdleState(State):
    def __init__(self):
        pass

    def step(self):
        pass

    def deactivate(self):
        pass

    @staticmethod
    def get_name():
        return "Idle State"