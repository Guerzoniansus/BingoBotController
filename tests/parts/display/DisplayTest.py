import random

from parts.display import Display

while True:
    number = random.randint(0, 76)
    Display.show_bingo_number_on_display(number)