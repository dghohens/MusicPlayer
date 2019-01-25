""" This is the starting file for the Terminal Tunes program.
"""

import msvcrt, configparser, FileSelection, WindowDisplay, Player2, vlc

config = configparser.ConfigParser()
config.read('playerConfig')

# File initialization. Program will start in file mode.
mode = 'file'
parent_dir = config['Directories']['Base directory']
current_dir = parent_dir
dircounter = 0
dirlist = []
playerinst = None


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
    # def file_update(current_working_directory, dircount, directorylist, action = ''):
    # return current_dir, select_dir, dirlist, dircount, subdirectories, selected_dir, selected_subdirectories
    directories = FileSelection.file_update(current_directory, dircount, directorylist, action)
    dircount = directories[3]
    # def file_window(subdirs, selected_dir, selected_subdirs, dircount):
    WindowDisplay.file_window(directories[4], directories[1], directories[6], dircount)
    return directories

# Song playing interface

# Initialize music player and get all the startup errors out
Player2.playsong('', '')

dirs = fileint(parent_dir, dircounter, dirlist)

# Main loop
while True:
    dircounter = dirs[3]
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    if key == 75 and (dirs[0] == parent_dir or dirs[0] == parent_dir + '\\'):
        print('You are at the root music directory!')
        pass
    elif key in [72, 75, 77, 80]:
        dirs = fileint(dirs[0], dirs[3], dirs[2], action = key_press(key))
        pass
    elif key in [13, 115, 32]:
        playerinst = Player2.playsong((dirs[0] + '\\' + dirs[1]), key_press(key), playerinst)
    elif key == 17:
        break
