# Описать функцию PowerA234(параметры), вычисляющую вторую, третью и четвертую
# степень числа A и возвращающую эти степени соответственно в переменные B, C и D. С
# помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.

def PowerA234(a):
    b = pow(a, 2)
    c = pow(a, 3)
    d = pow(a, 4)
    return b, c, d
i = 1
while i <= 5:
    i += 1
    b, c, d = PowerA234(i)
    print('a = {}, b = {}, c = {}, d = {}'.format(i, b, c, d))