from parts.display import Display

while True:
    value = input().split(' ')
    Display.show_vu(int(value[0]), int(value[1]), value[2])
