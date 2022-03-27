# Дан список A размера N и целые числа K и L (1 < K< L < N). Переставить в обратном
# порядке элементы списка, расположенные между элементами AK и AL, не включая эти
# элементы

from random import randint
A = []
# n = int(input('Кол-во символов: '))
n = 10
print(f'Длина списка: {n}')
l = randint(n/2, n)
k = randint(0, n/2)
for i in range(10):
    A.append(randint(0,n))
print(f'Верхняя граница значений списка: {l}')
print(f'Нижняя граница значений списка: {k}')
print(f'Список: {A}')
new = []
for i in A:
    if i<l and i>k:
        new.append(i)
print(f'Элементы списка, расположенные между l и k: {list(reversed(new))}')