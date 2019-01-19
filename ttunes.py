""" This is the starting file for the Terminal Tunes program.
"""

import configparser, FileSelection, WindowDisplay, msvcrt

config = configparser.ConfigParser()
config.read('playerConfig')

# File initialization. Program will start in file mode.
mode = 'file'
parent_dir = config['Directories']['Base directory']
current_dir = parent_dir
dircounter = 0
dirlist = []



# Key press actions. This needs to be changed to pull info from the playerConfig file.
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


# File interface
def fileint(current_directory, dircount, directorylist, action = ''):
    directories = FileSelection.file_update(current_directory, dircount, directorylist, action)
    dircount = directories[0][3]
    WindowDisplay.file_window(directories[1][0], directories[1][1], directories[1][2], dircount)
    print(directories[1][0])
    print(current_directory)
    return directories

# Song playing interface

# Music player


dirs = fileint(parent_dir, dircounter, dirlist)

# Main loop
while True:
    dircounter = dirs[0][3]
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    if key in [72, 75, 77, 80]:
        print(dirs[1][0])
        dirs = fileint(dirs[1][0], dircounter, dirs[1][2], action = key_press(key))
    elif key == 17:
        break
