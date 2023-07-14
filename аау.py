from random import *

x1 = 4
x2 = 8

n = int(input('Введите количество элементов'))
s = [randint(1,10) for x in range(n)]#заполнение списка
print(s)
ns = [x for x in range(len(s)) if s[x] in x1<=x<=x2]

print(*ns)