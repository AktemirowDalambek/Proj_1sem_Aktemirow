# Дан список размера N. Найти номера тех элементов списка, которые больше своего
# правого соседа, и количество таких элементов. Найденные номера выводить в порядке
# их возрастания.

from random import randint

N = int(input("Введите кол-во символов:"))
a = []
for i in range(N):
    b = randint(1,100)
    a.append(b)
print(a)
bigger = []
for i in range(1, len(a)):
   # if i < len(a):
    if a[i]<a[i-1]:
        bigger.append(a[i-1])
print(f'Элементы списка, которые больше своего правого соседа: {sorted(bigger)}\nИх количество: {len(bigger)}')