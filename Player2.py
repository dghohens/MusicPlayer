""" Trying an alternative player, using python-vlc instead.
Documentation here: http://www.olivieraubert.net/vlc/python-ctypes/doc/index.html
"""

import vlc


def playsong(song, action, playerinstance = None):
    if playerinstance == None:
        player = vlc.MediaPlayer(song)
    else:
        print(playerinstance.audio_get_track_description())
        player = playerinstance
    if action == 'play':
        player.stop()
        player = vlc.MediaPlayer(song)
        player.play()
        #print(player)
    elif action == 'pauseplay':
        player.pause()
        #print(player)
    elif action == 'stop':
        player.stop()
        #print(player)
    return player


""" This is the part that actually plays music.
This should only be called from ttunes.py.
Most of this was taken from or inspired by the playsound library.
"""

from ctypes import c_buffer, windll
from random import random
from time   import sleep
from sys    import getfilesystemencoding

class PlaysoundException(Exception):
    pass

# Stealing from playsound to get song length, cause finding playback time from VLC is hard.
def songtime(song):
    def winCommand(*command):
        buf = c_buffer(255)
        command = ' '.join(command).encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
        # This was in the previous code. I don't understand why you'd want to raise this particular exception. This module doesn't seem to work without this though.
        if errorCode:
            print(errorCode)
            errorBuffer = c_buffer(255)
            windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
            exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                                '\n        ' + command.decode() +
                                '\n    ' + errorBuffer.value.decode())
            raise PlaysoundException(exceptionMessage)
        return buf.value
    alias = 'playsound_' + str(random())
    winCommand('open "' + song + '" alias', alias)
    winCommand('set', alias, 'time format milliseconds')
    durationInMS = winCommand('status', alias, 'length')
    totaldur = int(durationInMS)//1000
    # winCommand('play', alias, 'from 0 to', durationInMS.decode())
    return totaldur

""" This part displays the time remaining on songs. Not in use.
for i in range(1, totaldur):
    sleep(1)
    print('\r' + str(i//60) + ':' + '{:02}'.format(i%60) + '/' + str(totaldur//60) + ':' + '{:02}'.format(totaldur%60), end = '')
"""
