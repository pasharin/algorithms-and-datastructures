N = str(input("Введите строку N: "))

print("Строка \'%s\' имеет длину %d сиволов." % (N, len(N)))

subs_set = set()
for i in range(len(N)):
    for j in range(len(N) - 1 if i == 0 else len(N), i, -1):
        subs_set.add(hash(N[i:j]))

print("Количество различных подстрок в этой строке:", len(subs_set))