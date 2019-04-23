# Задача №2

x = int(input('Введите натуральное число: '))
even=odd=0
while x>0:
    if x%2 == 0:
        even += 1
    else:
        odd += 1
    x = x//10
print("четных - %d, нечетных - %d" % (even, odd))

# Задача №3

n = int(input('Введите число: '))
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)

# Задача №4

a = int(input('Введите число: '))
b = 1
c = 0
for i in range(a):
    b += c
    b /= -2
print(c)

# Задача №5

for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()

# Задача №6

from random import random
n = round(random() * 100)
i = 1
print("Я загадал число. Отгадайте его. У тебя 10 попыток")
while i <= 10:
    m = int(input(str(i) + '-я попытка: '))
    if m > n:
        print('Много')
    elif m < n:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)

# Задача №7

n = int(input())
s = 0
for i in range(1,n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)

# Задача №9

n = int(input("Введите число: "))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n>0:
        s += n%10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input("Введите число: "))
print('Число',max_m,'имеет максимальную сумму цифр:', max_s)