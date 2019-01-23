""" Trying an alternative player, using winsound instead.
"""

import winsound

def playsong(song):
    winsound.PlaySound(song, winsound.SND_FILENAME)
    pass
