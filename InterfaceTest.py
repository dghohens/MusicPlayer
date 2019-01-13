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

run = True
dircounter = 0
os.system('cls')


def key_press(inkey):
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    action = ''
    type = ''
    if key == 17:
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


def colors(fore = 'white', back = 'black'):
    fore = fore.lower()
    back = back.lower()
    # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
    # Fores
    if fore == 'black':
        print(Fore.BLACK, '', end='')
    if fore == 'red':
        print(Fore.RED, '', end='')
    if fore == 'green':
        print(Fore.GREEN, '', end='')
    if fore == 'yellow':
        print(Fore.YELLOW, '', end='')
    if fore == 'blue':
        print(Fore.BLUE, '', end='')
    if fore == 'magenta':
        print(Fore.MAGENTA, '', end='')
    if fore == 'cyan':
        print(Fore.CYAN, '', end='')
    if fore == 'white':
        print(Fore.WHITE, '', end='')
    # Backs down here
    if back == 'black':
        print(Back.BLACK, '', end='')
    if back == 'red':
        print(Back.RED, '', end='')
    if back == 'green':
        print(Back.GREEN, '', end='')
    if back == 'yellow':
        print(Back.YELLOW, '', end='')
    if back == 'blue':
        print(Back.BLUE, '', end='')
    if back == 'magenta':
        print(Back.MAGENTA, '', end='')
    if back == 'cyan':
        print(Back.CYAN, '', end='')
    if back == 'white':
        print(Back.WHITE, '', end='')
    pass


def actions(action):
    if action == 'nextdir':
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


def file_window(subdirs, selected_subdirs, selected_dir):
    global file_fore, background, midwidth, file_select
    colors(file_fore, background)
    os.system('cls')
    print('┌=[' + '{:^{midwidth}}'.format('Parent Folder Contents', midwidth = midwidth - 4) + ']=┐  ┌──[' + '{:^{midwidth}}'.format('Selected Folder Contents', midwidth = midwidth - 6) + ']──┐', end='')
    for i in range(session_height - 2):
        c = abbrev_list(subdirs)
        d = abbrev_list(selected_subdirs)
        a = abbrev_file(c[i])
        b = abbrev_file(d[i])
        # https://stackoverflow.com/questions/29044940/how-can-you-use-a-variable-name-inside-a-python-format-specifier
        if subdirs[i] == selected_dir:
            print('\n' + '│', end='')
            colors(file_fore, file_select)
            print('{:{midwidth}}'.format(a, midwidth=midwidth - 4), end='')
            colors(file_fore, background)
            print('│  │' + '{:{midwidth}}'.format(b, midwidth=midwidth) + '│', end='')
        else:
            print('\n' +'│' + '{:{midwidth}}'.format(a, midwidth = midwidth) + '│  │' + '{:{midwidth}}'.format(b, midwidth = midwidth) + '│', end='')
        # print('\n' +'│' + '{:{}}'.format(a, midwidth) + '│ │' + '{:{}}'.format(b, midwidth) + '│', end = '')
    #print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    #print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')
    print('\n' + '└' + '─' * midwidth + '┘  └' + '─' * midwidth + '┘')


def get_dir(current_working_directory, selected_directory = None):
    subdirs = os.listdir(current_working_directory)
    if selected_directory == None:
        selected_directory = subdirs[0]
    selected_subdirs = os.listdir(current_working_directory + '\\' + selected_directory)
    return subdirs, selected_subdirs


def dirchange(select_dir=get_dir(current_working_directory=parent_directory), action = '', dir_list = []):
    global parent_directory, dircounter
    run = True
    dirs = get_dir(parent_directory)
    if action == 'downlevel':
        dir_list.append(select_dir)
    if action == 'uplevel':
        try:
            del(dir_list[-1])
        except IndexError:
            print('You are at the root music directory!')
    current_dir = parent_directory + '\\'.join(dir_list)
    if action == 'nextdir':
        try:
            dircounter += 1
            select_dir = dirs[0][dircounter]
        except IndexError:
            dircounter = 0
            selected_dir = dirs[0][dircounter]
        dirs = get_dir(parent_directory, select_dir)
        file_window(dirs[0], dirs[1], select_dir)
    if action == 'prevdir':
        try:
            dircounter -= 1
            select_dir = dirs[0][dircounter]
        except IndexError:
            dircounter = -1
            select_dir = dirs[0][dircounter]
        dirs = get_dir(parent_directory, select_dir)
        file_window(dirs[0], dirs[1], select_dir)
    if action == 'quit':
        run = False
    return current_dir, select_dir, dirs, run, dir_list


directories = dirchange()
file_window(directories[2][0], directories[2][1], directories[1])


while run:
    # https://stackoverflow.com/questions/12175964/python-method-for-reading-keypress
    key = ord(msvcrt.getch())
    if key == 224:
        key = ord(msvcrt.getch())
    if key in [72, 75, 77, 80, 17]:
        directories = dirchange(directories[1], key_press(key), directories[4])
        file_window(directories[2][0], directories[2][1], directories[1])
    '''
    if key_press(key) == 'nextdir':
        try:
            dircounter += 1
            selected_dir = dirs[0][dircounter]
        except IndexError:
            dircounter = 0
            selected_dir = dirs[0][dircounter]
        dirs = get_dir(parent_directory, selected_dir)
        os.system('cls')
        file_window(dirs[0], dirs[1], selected_dir)
    if key_press(key) == 'prevdir':
        try:
            dircounter -= 1
            selected_dir = dirs[0][dircounter]
        except IndexError:
            dircounter = -1
            selected_dir = dirs[0][dircounter]
        dirs = get_dir(parent_directory, selected_dir)
        os.system('cls')
        file_window(dirs[0], dirs[1], selected_dir)
    if key_press(key) == 'quit':
        run = False
        break
    '''

# When a key is pressed, clear screen and redraw https://stackoverflow.com/questions/2084508/clear-terminal-in-python