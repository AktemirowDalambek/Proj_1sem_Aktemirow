# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».

import re

with open('Writer.txt', 'r+', encoding='utf-8') as file:
    text = file.read()

print(text)

p = re.compile(f"(^[А-Я]\w+|^[А-Я]\S+)\s[А-Я]\W[А-Я]\W", re.M)
writers = p.findall(text)

print(writers, end='\n')
print(f'Количество писателей: {len(writers)}\n\n')

text = re.sub(r'([Рр]оманов)(\s|\W)', r'произведений\2', text)
text = re.sub(r'([Рр]оман)(\s|\W)', r'произведение\2', text)
text = re.sub(r'([Рр]омана)(\s|\W)', r'произведения\2', text)
text = re.sub(r'([Рр]оманы)(\s|\W)', r'произведения\2', text)

with open('NewWriter.txt', 'w+', encoding='utf-8') as new_file:
    new_file.write(f"{text}")