# Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
# получить новый список, в котором длина слов не превышает 5 символов.


name_list = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
new_list = [i for i in name_list if len(i) <= 5]
print('Список имён, длина которых не превышает 5 символов: ', new_list)