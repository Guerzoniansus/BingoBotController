from pyzbar import pyzbar

import Constants

if not Constants.USING_WEBOTS:
    from parts.vision.RaspberryCamera import RaspberryCamera
else:
    from parts.vision.WebotsCamera import WebotsCamera


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    return None if len(barcodes) == 0 else barcodes[0].data.decode('utf-8')


def get_code():
    camera_instance = RaspberryCamera.get_instance() if not Constants.USING_WEBOTS else WebotsCamera
    code = None

    while code is None:
        frame = camera_instance.read_frame()
        code = read_barcodes(frame)

    return code


def get_card():
    code = get_code()
    raw_card = [int(code[i:i + 2]) for i in range(0, len(code), 2)]
    raw_card.insert(12, -1)
    card = []

    for i in range(5):
        card.append(raw_card[i*5:i*5+5])
    return card
