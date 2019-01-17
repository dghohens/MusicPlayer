import os, configparser, msvcrt

config = configparser.ConfigParser()
config.read('playerConfig')

parent_directory = config['Directories']['Base directory']

dircounter = 0
dirlist = []


def abbrev_list(inlist):
    # Normalizes list length, adds "..." to beginning or end of list to indicate more files.
    global dircounter, session_height
    if len(inlist) > session_height - 2 and dircounter > session_height - 4:
        outlist = ['...']
        for i in range(session_height - 3):
            outlist.append(inlist[(i + dircounter) % (session_height - 4)])
        outlist.append('...')
        print(outlist)
    # Abbreviate list if it's too long
    elif len(inlist) > session_height - 2:
        outlist = inlist[0:session_height - 3]
        outlist.append('...')
    # Lengthen list if it's too short
    elif len(inlist) < session_height:
        outlist = inlist
        for i in range((session_height - 2) - len(inlist)):
            outlist.append('')
    else:
        outlist = inlist
    return outlist


def abbrev_file(infile):
    # Abbreviate files/folders that are longer than the display width, add "..." at the end. Shouldn't add "..." for under 4 characters.
    global midwidth
    if len(infile) > midwidth:
        outfile = infile[:midwidth - 3] + '...'
    else:
        outfile = infile
    return outfile


def select_abbrev_file(infile):
    # Shorten selected files/folders by 4 more than the abbrev_file function. This is because changing colors adds 2 spaces, and I can't figure out how to get rid of it.
    # Yes, I know this is hacky. Maybe I'll fix it one day.
    global midwidth
    if len(infile) > midwidth - 4:
        outfile = infile[:midwidth - 7] + '...'
    else:
        outfile = infile
    return outfile


def get_dir(current_working_directory, selected_directory=None):
    # Given the working directory and an optional selected directory, return the child and subchild directories.
    subdirs = os.listdir(current_working_directory)
    if selected_directory == None:
        selected_directory = subdirs[0]
    try:
        selected_subdirs = os.listdir(current_working_directory + '\\' + selected_directory)
    except NotADirectoryError:
        selected_subdirs = []
    return subdirs, selected_directory, selected_subdirs


def dirchange(current_working_directory, selected_directory, action=''):
    # Change directory based on an action. Maintains a directory list for going up/down levels.
    global parent_directory, dircounter, run, dirlist
    run = True
    if action == 'downlevel':
        dirlist.append(selected_directory)
        current_working_directory = parent_directory + '\\' + '\\'.join(dirlist)
        selected_directory = get_dir(current_working_directory)[1]
        return current_working_directory, selected_directory
    if action == 'uplevel':
        try:
            del(dirlist[-1])
            current_working_directory = parent_directory + '\\' + '\\'.join(dirlist)
            selected_directory = get_dir(current_working_directory)[1]
            return current_working_directory, selected_directory
        except IndexError:
            print('You are at the root music directory!')
            return current_working_directory, selected_directory
    if action == 'nextdir':
        try:
            dircounter += 1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory
        except IndexError:
            dircounter = 0
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory
    if action == 'prevdir':
        try:
            dircounter -= 1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory
        except IndexError:
            dircounter = -1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory
    if action == '':
        return current_working_directory, selected_directory


directories = get_dir(parent_directory)
file_window(directories[0], directories[1], directories[2])
currentdir = parent_directory
selected_dir = directories[1]
