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
    timeout = gevent.Timeout(1).start()
    #timeout.start()
    #try:
    a = input()
    print(a)
    sleep(0)
    pass
    #except gevent.Timeout:
     #   pass


while True:
    gevent.joinall([gevent.spawn(secadd), gevent.spawn(testinput)])
