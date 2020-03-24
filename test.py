from datetime import date, timedelta
import time
import math
import string
import random

date= date.today()
print(date)

date1 = timedelta(days=0)
print(date1)

print(date-date1)

time=time.time()*1000
print(time)  #返回当前时间的时间戳（1970纪元后经过的浮点秒数）。*1000
print(math.floor(time) )#返回小于或等于一个给定数字的最大整数

timestamp = str(math.floor(time))
print(timestamp)


print(string.ascii_uppercase)
print(string.digits)

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

random_generator=random_generator()
print(random_generator)

nonce = timestamp + random_generator

print(nonce)
x = {random.choice('123abcggg457') for x in range(6)}
print(x)
