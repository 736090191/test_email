from functools import reduce
__author__ = 'Administrator'

# def is_odd(n):
#     return n % 2 == 1
#
# s = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# for i in s:
#     print(i)

# d = {"a":1,"b":2}
# print((list(d.keys())))
# print(d.keys())


# a = ['name','age']
# b = ['xiaobai',18]
# d = ".."
# d.join(zip(a, b))
# print(d)
# x="aaa"
# isinstance(x, str)

import time
f = open("1112.txt","a")
# print(type(str(time.time())))
f.write(str(time.time()) + "\n")
f.close()

import os
