""" Testing gevent
"""

import gevent
from gevent import sleep

seconds = 0

def secadd():
    global seconds
    seconds += 1
    print(seconds)
    sleep(1)
    pass


def testinput():
    a = input()
    print(a)
    sleep(0)


while True:
    gevent.joinall([gevent.spawn(secadd), gevent.spawn(testinput)])
