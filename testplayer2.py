"""Python 3 CLI audio player
"""

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
totaldur = int(durationInMS)//1000
winCommand('play', alias, 'from 0 to', durationInMS.decode())

for i in range(1, totaldur):
    sleep(1)
    print('\r' + str(i//60) + ':' + '{:02}'.format(i%60) + '/' + str(totaldur//60) + ':' + '{:02}'.format(totaldur%60), end = '')
