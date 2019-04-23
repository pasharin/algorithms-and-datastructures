
#####
print('Задача №1')
print('Введите трехзначное число')
n = int(input(' n = '))
print('Сумма введеного числа: ', n + n)
print('Произведение введеного числа: ', n * n)
######

print('Задача №2')
a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))
print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d << 2 = %d (%s)" % (b, b << 2, bin(b << 2)))
print("%d >> 2 = %d (%s)" % (b, b >> 2, bin(b >> 2)))

#####

print('Задача №3')
print("Координаты точки A(x1;y1):")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
print("Координаты точки B(x2;y2):")
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(" y = %.2f*x + %.2f" % (k, b))

######
print('Задача №5')
a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'{a, b}')
print(f'Между буквами символов: {abs(a - b) - 1}')

#####
print('Задача №6')
n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Это буква', chr(n))

#####
print('Задача №8')
y = int(input())
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

#####
print('Задача №9')
a = int(input('Введите первое чистло: '))
b = int(input('Введите второе чистло: '))
c = int(input('Введите третье чистло: '))

if b < a < c or c < a < b:
    print('Среднее значение:', a)
elif a < b < c or c < b < a:
    print('Среднее значение:', b)
else:
    print('Среднее значение:', c)

