""" You know what this is, ya chump.
"""

import gevent
seconds = 0


def test1():
    global seconds
    timeout = gevent.Timeout(1).start()
    seconds += 1
    print(seconds)
    try:
        a = input()
        print(a)
        pass
    except gevent.Timeout:
        test1()



while True:
    test1()
