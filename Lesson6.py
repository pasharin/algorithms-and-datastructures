from memory_profiler import profile
from random import random

y = 2009
@profile #код из дз №1
def year(y):
    if y % 4 != 0:
        print("Обычный")
    elif y % 100 == 0:
        if y % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Високосный")
year(y)

'''
Line #    Mem usage    Increment   Line Contents
================================================
     5     11.6 MiB     11.6 MiB   @profile #код из дз №1
     6                             def year(y):
     7     11.6 MiB      0.0 MiB       if y % 4 != 0:
     8     11.6 MiB      0.0 MiB           print("Обычный")
     9                                 elif y % 100 == 0:
    10                                     if y % 400 == 0:
    11                                         print("Високосный")
    12                                     else:
    13                                         print("Обычный")
    14                                 else:
    15                                     print("Високосный")
'''

@profile #попробовал немного сократить код из дз №1
def year_2(y):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        print('Високосный')
    else:
        print('Обычный')
year_2(y)

'''
Line #    Mem usage    Increment   Line Contents
================================================
    18     11.6 MiB     11.6 MiB   @profile #попробовал немного сократить код из дз №1
    19                             def year_2(y):
    20     11.6 MiB      0.0 MiB       if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    21                                     print('Високосный')
    22                                 else:
    23     11.6 MiB      0.0 MiB           print('Обычный')
'''


n = 100 #код из дз №3
@profile
def num(n):
    arr = [0] * n
    even = []
    for i in range(n):
        arr[i] = int(random() * 10) + 10
        if arr[i] % 2 == 0:
            even.append(i)
    print(arr)
    print('Индексы четных элементов: ', even)
num(n)

'''
Line #    Mem usage    Increment   Line Contents
================================================
    27     11.6 MiB     11.6 MiB   @profile
    28                             def num(n):
    29     11.6 MiB      0.0 MiB       arr = [0] * n
    30     11.6 MiB      0.0 MiB       even = []
    31     11.6 MiB      0.0 MiB       for i in range(n):
    32     11.6 MiB      0.0 MiB           arr[i] = int(random() * 10) + 10
    33     11.6 MiB      0.0 MiB           if arr[i] % 2 == 0:
    34     11.6 MiB      0.0 MiB               even.append(i)
    35     11.6 MiB      0.0 MiB       print(arr)
    36     11.6 MiB      0.0 MiB       print('Индексы четных элементов: ', even)
'''

# Разработка на PyCharm, Python 3.7.3
# ОС MacOS Mojave 64-бит