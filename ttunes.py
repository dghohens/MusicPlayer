""" This is the starting file for the Terminal Tunes program.
"""

import msvcrt, configparser, FileSelection, WindowDisplay, Player2, gevent
from gevent import sleep

config = configparser.ConfigParser()
config.read('playerConfig')

# File initialization. Program will start in file mode.
mode = 'file'
parent_dir = config['Directories']['Base directory']
current_dir = parent_dir
dircounter = 0
dirlist = []
playerinst = None
seconds = 0


# Key press actions. This needs to be changed to pull info from the playerConfig file.
def key_press(inkey):
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    action = ''
    type = ''
    if inkey == 17:
        # No longer in use, keeping it so I remember that ctrl+q is ASCII code 17.
        # Quit
        action = 'quit'
    if inkey == 32:
        # pause/play
        action = 'pauseplay'
    if inkey == 115:
        # stop
        action = 'stop'
    if inkey == 100:
        # skip forward
        action = 'fskip'
    if inkey == 97:
        # skip backward
        action = 'bskip'
    if inkey == 120:
        # toggle shuffle
        action = 'shuffleonoff'
    if inkey == 61:
        # turn up volume
        action = 'upvolume'
    if inkey == 45:
        # turn down volume
        action = 'downvolume'
    if inkey == 62:
        # play faster
        action = 'speedup'
    if inkey == 60:
        # play slower
        action = 'slowdown'
    if inkey == 27:
        # Go to file view
        action = 'fileview'
    if inkey == 63:
        # display help page
        action = 'help'
    if inkey == 80:
        # Select next directory
        action = 'nextdir'
    if inkey == 72:
        # select previous directory
        action = 'prevdir'
    if inkey == 75:
        # Go up a level
        action = 'uplevel'
    if inkey == 77:
        # Go down a level
        action = 'downlevel'
    if inkey == 13:
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
    WindowDisplay.file_window(directories[4], directories[4][dircount], directories[6], dircount)
    return directories

# Song playing interface

# Initialize music player and get all the startup errors out
Player2.playsong('', '')

dirs = fileint(parent_dir, dircounter, dirlist)

# Main loop


def secondcount():
    global seconds
    sleep(1)
    seconds += 1
    print()
    print()
    print(seconds)
    return seconds


def main(dirs):
    global seconds
    secondcount()
    sleep(0)
    # seconds += 1
    print(seconds)
    dircounter = dirs[3]
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    if key == 75 and (dirs[0] == parent_dir or dirs[0] == parent_dir + '\\'):
        print('You are at the root music directory!')
        pass
    elif key in [72, 75, 77, 80]:
        dirs = fileint(dirs[0], dirs[3], dirs[2], key_press(key))
        dircounter = dirs[3]
        #print(dircounter)
        #print(dirs[3])
        #print(dirs[4][dircounter])
        # selected_directory = get_dir(current_working_directory)[0][dircounter]
        #     return subdirs, selected_directory, selected_subdirs
        pass
    elif key in [13, 115, 32]:
        playerinst = Player2.playsong((dirs[0] + '\\' + dirs[1]), key_press(key), playerinst)
        if key == 13:
            playback = True
    elif key == 17:
        print(seconds)
        pass
    else:
        secondcount()
        pass


while True:
    gevent.joinall([gevent.spawn(main(dirs)), gevent.spawn(secondcount)])
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    elif key == 17:
        break

# main(dirs)
