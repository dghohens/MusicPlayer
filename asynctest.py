""" Testing async
https://stackabuse.com/python-async-await-tutorial/
https://www.aeracode.org/2018/02/19/python-async-simplified/
"""

import os, time, asyncio

counter = 0

def timecount(count):
    count += 1
    time.sleep(1)
    os.system('cls')
    print(count)
    return count

async def testasync()

