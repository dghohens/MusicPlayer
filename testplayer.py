"""Python 3 CLI audio player
"""

from playsound import playsound

from ctypes import c_buffer, windll
from sys import getfilesystemencoding

file = 'K:\\Music\\Hotline Miami 2 OST\\Soundtrack\\49 Escape From Midwitch Valley.mp3'

#playsound(file)


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
        raise errorCodeException(exceptionMessage)
    return buf.value

durationInMS = winCommand('status', file, 'length')
print(durationInMS)

#playsound(file)
