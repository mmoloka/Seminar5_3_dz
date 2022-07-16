# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


n = int(input('Введите количество чисел в списке: '))
numbers1 = list()
numbers2 = list()
for i in range(n):
    numbers1.insert(0, randint(1, 9))


if n % 2 == 0:
    for j in range(n//2):
        numbers2.append(numbers1[j] * numbers1[-1-j])
else:
    for j in range(n//2):
        numbers2.append(numbers1[j] * numbers1[-1-j])
    numbers2.append(numbers1[n//2]**2)

print('Заданный список: ', numbers1)
print('Выходной список: ', numbers2)
