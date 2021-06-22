from parts.display import Display

while True:
    value = input().split(' ')
    Display.show_vu(value[0], value[1], value[2])
