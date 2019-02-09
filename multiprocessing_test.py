"""
Special thanks to Patrick K. for your assistance on this one!
"""

from multiprocessing import Process, Manager
import time


a = True


def secadd(lst_sec, song_dur):
    lst_sec = int(lst_sec[0])
    while lst_sec < song_dur:
        time.sleep(1)
        lst_sec += 1
        print(lst_sec)


def testinput():
    print('Enter your input:')
    x = input()
    if x.lower() == 'quit':
        out = False
    else:
        out = True
    print(x)
    return out


if __name__ == '__main__':  # execute the code below only if it is the main process (prevents subprocesses from executing code when using multiprocessing)

    manager = Manager()  # initialize the multiprocessing.Manager - Manager allows us to get information from the subprocesses back to the parent.

    seconds_var = manager.list("0")

    total_run = 5

    # https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/
    # https: // stackoverflow.com / questions / 5697305 / python - command - line - input - in -a - process
    p1 = Process(target=secadd, args=(seconds_var, total_run))
    p1.start()

    while a == True:
        a = testinput()

