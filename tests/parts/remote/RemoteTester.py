from parts.remote.RemoteControl import RemoteControl
from tests.parts.remote.TestListener import TestListener


listener = TestListener()
remote_control = RemoteControl.get_instance()
remote_control.add_listener(listener)

remote_control.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    remote_control.stop()
    print("Keyboard interrupted the program!")
