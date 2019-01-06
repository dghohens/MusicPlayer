"""Python 3 CLI audio player
"""

from playsound import playsound

file = 'K:\\Music\\Hotline Miami 2 OST\\Soundtrack\\49 Escape From Midwitch Valley.mp3'

from ctypes import c_buffer, windll
from random import random
from time   import sleep
from sys    import getfilesystemencoding

def winCommand(*command):
    buf = c_buffer(255)
    command = ' '.join(command).encode(getfilesystemencoding())
    errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
    if errorCode:
        errorBuffer = c_buffer(255)
        windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
        exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                            '\n        ' + command.decode() +
                            '\n    ' + errorBuffer.value.decode())
        raise PlaysoundException(exceptionMessage)
    return buf.value

alias = 'playsound_' + str(random())
winCommand('open "' + file + '" alias', alias)
winCommand('set', alias, 'time format milliseconds')
durationInMS = winCommand('status', alias, 'length')
print(durationInMS)
totaldur = int(durationInMS)//1000
print(totaldur)
# winCommand('play', alias, 'from 0 to', durationInMS.decode())

for i in range(totaldur):
    sleep(1)
    print(i, '/', totaldur)
    winCommand('play', alias, 'from ', str((i * 1000)), ' to', str((i * 1000) + 1000 ))

#sleep(float(durationInMS) / 1000.0)