""" Testing gevent
"""

import gevent
from gevent import sleep

def foo():
    for i in range(1,11):
        print(i)
        sleep(5)


def bar():
    for j in range(2,22,2):
        print(j)
        sleep(0)


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
