from colorama import init, Fore, Back, Style
import os

init()

session_width = 80
session_height = 25

file = '<filename>'

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


def player_window():
    print(Fore.YELLOW, '')
    print(Back.BLACK, '')
    print('┌=[' + '    Artist name - Album name    ' + ']=┐ ┌───[' + '   Artist name - Song name   ' + ']───┐', end = '')
    print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')


def file_window(subdirs, selected_subdirs):
    midwidth = (session_width - 6)//2
    print(Fore.GREEN, '')
    print(Back.BLACK, '')
    print('┌=[' + '     Current Folder Contents    ' + ']=┐ ┌───[' + '  Selected Folder Contents   ' + ']───┐', end='')
    for i in range(session_height - 2):
        c = abbrev_list(subdirs)
        d = abbrev_list(selected_subdirs)
        a = c[i]
        b = d[i]
        if len(a) > 36:
            a = a[0:32] + '...'
        if len(b) > 36:
            b = b[0:32] + '...'
        print('\n' +'│' + {midwidth}.format(a) + '│  │' + {midwidth}.format(b) + '│', end = '')
    #print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
    #print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')
    print('\n' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')

def get_dir(current_working_directory, selected_directory):
    subdirs = os.listdir(current_working_directory)
    selected_subdirs = os.listdir(selected_directory)
    return subdirs, selected_subdirs

dirs = get_dir('<parentdir>', '<subdir>')

print(len(dirs[0]), len(dirs[1]))
file_window(dirs[0], dirs[1])