# Используя словарь посчитать количество уникальных слов в заданном
# предложении «Изучаем язык Питон». Вывести на экран каждую пару
# «ключ:значение»

stroke = 'Изучаем язык Питон'
d = stroke.split()
d1 = {}
for i in d:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i]+=1
print(d1)
k = 0
for i in d1:
    if d1[i] == 1:
        k+=1
print('Количество уникальных слов в заданном предложении:', k)
for i in d1.items():
    print(i)