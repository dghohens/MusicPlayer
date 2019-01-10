from colorama import init, Fore, Back, Style
import os, configparser, msvcrt

init()

config = configparser.ConfigParser()
config.read('playerConfig')

session_width = int(config['Interface sizing']['Session width'])
session_height = int(config['Interface sizing']['Session height'])
midwidth = (session_width - 6)//2

background = config['Interface colors']['Background']
file_fore = config['Interface colors']['File foreground']
file_select = config['Interface colors']['File selection']

parent_directory = config['Directories']['Base directory']

def key_press(key):
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    if key == 17:
        # Quit
        pass
    if key == 32:
        # pause/play
        pass
    if key == 115
        # stop
        pass
    if key == 100:
        # skip forward
        pass
    if key == 97:
        # skip backward
        pass
    if key == 120:
        # toggle shuffle
        pass
    if key == 61:
        # turn up volume
        pass
    if key == 45:
        # turn down volume
        pass
    if key == 62:
        # play faster
        pass
    if key == 60:
        # play slower
        pass
    if key == 27:
        # Go to file view
        pass
    if key == 63:
        # display help page
        pass
    if key == 80:
        # Select next directory
    if key == 72:
        # select previous directory
        pass
    if key == 75:
        # Go up a level
        pass
    if key == 77:
        # Go down a level
        pass
    if key == 13:
        # start playing
        pass
    pass


def abbrev_list(inlist):
    # Abbreviate list if it's too long
    if len(inlist) > session_height - 2:
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
    global midwidth
    if len(infile) > midwidth:
        outfile = infile[:midwidth - 3] + '...'
    else:
        outfile = infile
    return outfile


def player_window():
    print(Fore.YELLOW, '')
    print(Back.background, '')
    print('┌=[' + '    Artist name - Album name    ' + ']=┐ ┌───[' + '   Artist name - Song name   ' + ']───┐', end = '')
    print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')


def file_window(subdirs, selected_subdirs):
    global file_fore, background, midwidth
    print(file_fore, '')
    print(background, '')
    print('┌=[' + '{:^{midwidth}}'.format('Parent Folder Contents', midwidth = midwidth - 4) + ']=┐  ┌──[' + '{:^{midwidth}}'.format('Selected Folder Contents', midwidth = midwidth - 6) + ']──┐', end='')
    for i in range(session_height - 2):
        c = abbrev_list(subdirs)
        d = abbrev_list(selected_subdirs)
        a = abbrev_file(c[i])
        b = abbrev_file(d[i])
        # https://stackoverflow.com/questions/29044940/how-can-you-use-a-variable-name-inside-a-python-format-specifier
        print('\n' +'│' + '{:{midwidth}}'.format(a, midwidth = midwidth) + '│  │' + '{:{midwidth}}'.format(b, midwidth = midwidth) + '│', end = '')
        # print('\n' +'│' + '{:{}}'.format(a, midwidth) + '│ │' + '{:{}}'.format(b, midwidth) + '│', end = '')
    #print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    #print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')
    print('\n' + '└' + '─' * midwidth + '┘  └' + '─' * midwidth + '┘')

def get_dir(current_working_directory, selected_directory = None):
    subdirs = os.listdir(current_working_directory)
    if selected_directory == None:
        selected_directory = current_working_directory + subdirs[0]
    selected_subdirs = os.listdir(selected_directory)
    return subdirs, selected_subdirs

dirs = get_dir(parent_directory)
selected_dir = parent_directory + dirs[0][0]

file_window(dirs[0], dirs[1])


dirs = get_dir(parent_directory, selected_dir)
# https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
key = ord(msvcrt.getch())
key = ord(msvcrt.getch())
print(key)

if key == 80:
    selected_dir = parent_directory + dirs[0][1]
    dirs = get_dir(parent_directory, selected_dir)
    os.system('cls')
    file_window(dirs[0], dirs[1])

# When a key is pressed, clear screen and redraw https://stackoverflow.com/questions/2084508/clear-terminal-in-python