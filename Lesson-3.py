#Задача 1

a = [0]*8
for i in range(2,100):
    for b in range(2,10):
        if i%b == 0:
            a[b-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

#Задача 3

from random import random

N = int(input('Введите число: '))
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)

x = f'arr {imx + 1} = {mn} arr {imx + 1}= {mx}'
print(x)
arr[imn], arr[imx] = arr[imx], arr[imn]

#Задача 4

from random import random

N = int(input('Введите число: '))
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

#Задача 5

from random import random

N = int(input('Введите число: '))
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

#Задача 2

from random import random

N = int(input('Введите число: '))
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)