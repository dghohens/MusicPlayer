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
        player.play()
        print(player)
    elif action == 'pauseplay':
        player.pause()
        print(player)
    elif action == 'stop':
        player.stop()
        player = None
    return player
