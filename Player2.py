""" Trying an alternative player, using python-vlc instead.
"""

import vlc


def playsong(song, action):
    player = vlc.MediaPlayer(song)
    if action == 'play':
        player.play()
    elif action == 'pauseplay':
        player.pause()
    elif action == 'stop':
        player.stop()
    pass
