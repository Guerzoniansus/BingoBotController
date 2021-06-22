from parts.MicroController import MicroController


def get_weight():
    return MicroController.get_instance().get_weight()
