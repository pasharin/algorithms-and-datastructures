import timeit

def myArr():
    n = 25
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = n // 10
print(timeit.timeit(myArr))
