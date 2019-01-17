""" This is the starting file for the Terminal Tunes program.
"""

import configparser

config = configparser.ConfigParser()
config.read('playerConfig')


# File interface

# Song playing interface

# Music player

# Key press actions
def key_press(inkey):
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    action = ''
    type = ''
    if key == 17:
        # No longer in use, keeping it so I remember that ctrl+q is ASCII code 17.
        # Quit
        action = 'quit'
    if key == 32:
        # pause/play
        action = 'pauseplay'
    if key == 115:
        # stop
        action = 'stop'
    if key == 100:
        # skip forward
        action = 'fskip'
    if key == 97:
        # skip backward
        action = 'bskip'
    if key == 120:
        # toggle shuffle
        action = 'shuffleonoff'
    if key == 61:
        # turn up volume
        action = 'upvolume'
    if key == 45:
        # turn down volume
        action = 'downvolume'
    if key == 62:
        # play faster
        action = 'speedup'
    if key == 60:
        # play slower
        action = 'slowdown'
    if key == 27:
        # Go to file view
        action = 'fileview'
    if key == 63:
        # display help page
        action = 'help'
    if key == 80:
        # Select next directory
        action = 'nextdir'
    if key == 72:
        # select previous directory
        action = 'prevdir'
    if key == 75:
        # Go up a level
        action = 'uplevel'
    if key == 77:
        # Go down a level
        action = 'downlevel'
    if key == 13:
        # start playing
        action = 'play'
    return action


# Main loop
while True:
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    if key in [72, 75, 77, 80]:
        directory_change = dirchange(currentdir, selected_dir, key_press(key))
        currentdir = directory_change[0]
        selected_dir = directory_change[1]
        directories = get_dir(currentdir, selected_dir)
        file_window(directories[0], directories[1], directories[2])
    elif key == 17:
        break
