from colorama import init, Fore, Back, Style

init()

print(Fore.YELLOW, '')
Back.BLACK
print('┌=[' + '    Artist name - Album name    ' + ']=┐ ┌───[' + '   Artist name - Song name   ' + ']───┐', end = '')
print(('\n' + '│' + ' ' * 36 + '│ │' + ' ' * 37 + '│') * 22)
print('\033[F' + '└' + '─' * 36 + '┘ └' + '─' * 37 + '┘')