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


def abbrev_list(inlist, dircounter):
    # Normalizes list length, adds "..." to beginning or end of list to indicate more items.
    global session_height
    if len(inlist) > session_height - 2 and dircounter > session_height - 4:
        outlist = ['...']
        for i in range(session_height - 3):
            outlist.append(inlist[(i + dircounter) % (session_height - 4)])
        outlist.append('...')
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


def abbrev_item(initem):
    # Abbreviate items that are longer than the display width, add "..." at the end. Shouldn't add "..." for under 4 characters.
    global midwidth
    if len(initem) > midwidth:
        outitem = initem[:midwidth - 3] + '...'
    else:
        outitem = initem
    return outitem


def select_abbrev_item(initem):
    # Shorten selected items by 4 more than the abbrev_item function. This is because changing colors adds 2 spaces, and I can't figure out how to get rid of it.
    # Yes, I know this is hacky. Maybe I'll fix it one day.
    global midwidth
    if len(initem) > midwidth - 4:
        outitem = initem[:midwidth - 7] + '...'
    else:
        outitem = initem
    return outitem


def file_window(subdirs, selected_dir, selected_subdirs, dircount):
    global file_fore, background, midwidth, file_select
    colors(file_fore, background)
    # When a key is pressed, clear screen and redraw https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls')
    print('┌=[' + '{:^{midwidth}}'.format('Current Folder Contents', midwidth = midwidth - 4) + ']=┐  ┌──[' + '{:^{midwidth}}'.format('Selected Folder Contents', midwidth = midwidth - 6) + ']──┐', end='')
    c = abbrev_list(subdirs, dircount)
    d = abbrev_list(selected_subdirs, dircount)
    for i in range(session_height - 2):
        a = abbrev_item(c[i])
        b = abbrev_item(d[i])
        # https://stackoverflow.com/questions/29044940/how-can-you-use-a-variable-name-inside-a-python-format-specifier
        if subdirs[i] == selected_dir:
            print('\n' + '│', end='')
            colors(file_fore, file_select)
            print('{:{midwidth}}'.format(select_abbrev_item(a), midwidth=midwidth - 4), end='')
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
