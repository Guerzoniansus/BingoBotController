import random
import time
from parts.display import Display

while True:
    for i in range(0, 5):
        number = random.randint(0, 75)
        Display.show_bingo_number_on_display(number)
        time.sleep(5)

    for i in range(0, 10):
        Display.show_vu(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
        time.sleep(0.5)
