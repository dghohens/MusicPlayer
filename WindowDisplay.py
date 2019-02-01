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
player_fore = config['Interface colors']['Music foreground']
player_select = config['Interface colors']['Music selection']

os.system('cls')


# Can't put colors from config file directly into colorama, so we gotta do this silly hack.
def colors(fore = 'white', back = 'black'):
    fore = fore.lower()
    back = back.lower()
    print(fore, back)
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
    # If the length of the list is more than the height of the display, and the selection is past the normal last element,
    # add ... to the beginning, display all the entries including the selection and add ... to the end.
    if len(inlist) > session_height - 2 and dircounter > session_height - 4:
        outlist = ['...']
        if dircounter != -1 and dircounter != len(inlist) - 1:
            # I literally just figured this out by adding and subtracting numbers to the range in a pseudorandom way. Mess with this at your own peril.
            for i in range((dircounter - session_height + 5), dircounter + 1):
                outlist.append(inlist[i])
            outlist.append('...')
        else:
            for i in range((dircounter - session_height + 4), dircounter + 1):
                outlist.append(inlist[i])
    # This is to get reverse scroll to work correctly
    elif len(inlist) > session_height - 2 and dircounter < 0 and abs(dircounter) < session_height - abs(dircounter):
        outlist = ['...']
        if dircounter != -1 and dircounter != len(inlist) - 1:
            for i in range((dircounter - session_height + 5), dircounter + 1):
                outlist.append(inlist[i])
            outlist.append('...')
        else:
            for i in range((dircounter - session_height + 4), dircounter + 1):
                outlist.append(inlist[i])
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
        if c[i] == selected_dir:
            print('\n' + '│', end='')
            colors(file_fore, file_select)
            print('{:{midwidth}}'.format(select_abbrev_item(a), midwidth=midwidth - 4), end='')
            colors(file_fore, background)
            print('│  │' + '{:{midwidth}}'.format(b, midwidth=midwidth) + '│', end='')
        else:
            print('\n' +'│' + '{:{midwidth}}'.format(a, midwidth = midwidth) + '│  │' + '{:{midwidth}}'.format(b, midwidth = midwidth) + '│', end='')
    print('\n' + '└' + '─' * midwidth + '┘  └' + '─' * midwidth + '┘')
    pass


# Still gotta build this one out
def player_window(subdirs, dircount, playlist):
    global player_fore, background, midwidth, player_select
    colors(player_fore, background)
    os.system('cls')
    c = abbrev_list(subdirs, dircount)
    d = abbrev_list(playlist, dircount)
    e = abbrev_list(playlist, 0)
    curtime = 0
    totaltime = 0
    print('┌=[' + '{:^{midwidth}}'.format('Current Folder', midwidth = midwidth - 4) + ']=┐  ┌──[' + '{:^{midwidth}}'.format('Current Song', midwidth = midwidth - 6) + ']──┐', end='')
    print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[0]), midwidth=midwidth) + '│  │' + '{:{midwidth}}'.format('Time:    ', curtime, ':', totaltime, midwidth=midwidth) + '│', end='')
    print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[1]), midwidth=midwidth) + '│  └' + '─' * midwidth + '┘', end = '')
    print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[2]), midwidth=midwidth) + '│  ┌──[' + '{:^{midwidth}}'.format('Current Selection', midwidth = midwidth - 6) + ']──┐', end='')
    for i in range(3,7):
        print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[i]), midwidth=midwidth) + '│  |' + '{:^{midwidth}}'.format(abbrev_item(d[i-3]), midwidth=midwidth) + '|', end='')
    print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[8]), midwidth=midwidth) + '│  └' + '─' * midwidth + '┘', end = '')
    print('\n' + '│' + '{:{midwidth}}'.format(abbrev_item(c[1]), midwidth=midwidth) + '│  ┌──[' + '{:^{midwidth}}'.format('Playlist', midwidth = midwidth - 6) + ']──┐', end='')
    print(('\n' + '│' + ' ' * midwidth + '│  │' + ' ' * midwidth + '│') * 11, end = '')
    # 2nd column should also include selection info and playlist
    # print('┌=[' + '    Artist name - Album name    ' + ']=┐ ┌───[' + '   Artist name - Song name   ' + ']───┐', end = '')
    print(('\n' + '│' + ' ' * midwidth + '│  │' + ' ' * midwidth + '│') * 11)
    print('\033[F' + '└' + '─' * midwidth + '┘  └' + '─' * midwidth + '┘')
