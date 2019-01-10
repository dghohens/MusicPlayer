import msvcrt

while True:
    key = ord(msvcrt.getch())
    print(key)
    key = ord(msvcrt.getch())
    print(key)
    if key == 3:
        break