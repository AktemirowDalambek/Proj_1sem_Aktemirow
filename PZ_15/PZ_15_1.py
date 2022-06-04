# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних сроках и столбцах матрицы Matr2 произвольного размера.

from numpy import *

matr2 = array([[18, 20, 22, 17], [11, 18, 21, 18], [18, 17, 23, 22], [12, 22, 20, 18]])
print('Исходная матрица:')
for i in matr2:
    print(*i)
matr2 = delete(matr2, [0], 0)
matr2 = delete(matr2, [-1], 0)
matr2 = delete(matr2, s_[0], 1)
matr2 = delete(matr2, s_[-1], 1)
matr1 = matr2
print('Полученная матрица:')
for i in matr1:
    print(*i)