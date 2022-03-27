# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Отрицательные нечетные элементы:
# Сумма отрицательных нечетных элементов:
# Среднее арифметическое отрицательных нечетных элементов:

from random import randint   # Генерируем список рандомной длины случайных чисел.
my_list = list(str(randint(-100, 100)) for i in range(randint(10, 20)))
print(my_list)

with open("new_file.txt", "w+", encoding="utf-8") as file:   # Помещаем в файл список
    file.writelines(' '.join(my_list))

with open("new_file.txt", "r+", encoding="utf-8") as file:
    file_list = list(file.read().split(' '))
    print(file_list)
    with open("main_file.txt", "w+", encoding="utf-8") as main:
        neg_nt_even = list(int(i) for i in file_list if int(i) < 0 and int(i) % 2 == 1)
        print(neg_nt_even)
        main.writelines(f"Initial Data:\n{' '.join(file_list)} \n\n"
                        f"Amount of elements:\n {len(file_list)}\n\n"
                        f"Negative not even elements:\n {' '.join([str(i) for i in neg_nt_even])}\n\n"
                        f"Sum of negative not even elements:\n {sum(neg_nt_even)}\n\n"
                        f"Arithmetical mean:\n {round(sum(neg_nt_even) / len(neg_nt_even), 2)}")