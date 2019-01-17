""" This program just displays the window. This should be called from either FileSelection or MusicSelection.
"""

from colorama import init, Fore, Back, Style
import os, configparser

init()

config = configparser.ConfigParser()
config.read('playerConfig')

session_width = int(config['Interface sizing']['Session width'])
session_height = int(config['Interface sizing']['Session height'])
midwidth = (session_width - 6)//2

background = config['Interface colors']['Background']
file_fore = config['Interface colors']['File foreground']
file_select = config['Interface colors']['File selection']

os.system('cls')


# Can't put colors from config file directly into colorama, so we gotta do this silly hack.
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

def file_window(subdirs, selected_dir, selected_subdirs):
    global file_fore, background, midwidth, file_select
    colors(file_fore, background)
    # When a key is pressed, clear screen and redraw https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls')
    print('┌=[' + '{:^{midwidth}}'.format('Current Folder Contents', midwidth = midwidth - 4) + ']=┐  ┌──[' + '{:^{midwidth}}'.format('Selected Folder Contents', midwidth = midwidth - 6) + ']──┐', end='')
    c = abbrev_list(subdirs)
    d = abbrev_list(selected_subdirs)
    for i in range(session_height - 2):
        a = abbrev_file(c[i])
        b = abbrev_file(d[i])
        # https://stackoverflow.com/questions/29044940/how-can-you-use-a-variable-name-inside-a-python-format-specifier
        if subdirs[i] == selected_dir:
            print('\n' + '│', end='')
            colors(file_fore, file_select)
            print('{:{midwidth}}'.format(select_abbrev_file(a), midwidth=midwidth - 4), end='')
            colors(file_fore, background)
            print('│  │' + '{:{midwidth}}'.format(b, midwidth=midwidth) + '│', end='')
        else:
            print('\n' +'│' + '{:{midwidth}}'.format(a, midwidth = midwidth) + '│  │' + '{:{midwidth}}'.format(b, midwidth = midwidth) + '│', end='')
        # print('\n' +'│' + '{:{}}'.format(a, midwidth) + '│ │' + '{:{}}'.format(b, midwidth) + '│', end = '')
    #print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    #print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')
    print('\n' + '└' + '─' * midwidth + '┘  └' + '─' * midwidth + '┘')
    pass


# Still gotta build this one out
def player_window():
    print(Fore.YELLOW, '')
    print(Back.background, '')
    print('┌=[' + '    Artist name - Album name    ' + ']=┐ ┌───[' + '   Artist name - Song name   ' + ']───┐', end = '')
    print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')
