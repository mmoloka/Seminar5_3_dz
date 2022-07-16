# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Введите количество чисел в списке: '))
numbers = list()
for i in range(n):
    numbers.append(float(input(f'Введите вещественное число - {i + 1} элемент списка: ')))

max = numbers[0] - int(numbers[0])
min = 0
for j in range(1, n):
    if numbers[j] - int(numbers[j]) > max:
        min = max
        max = numbers[j] - int(numbers[j])
    if numbers[j] - int(numbers[j]) < min:
        min = numbers[j] - int(numbers[j])

print('Заданный список: ', numbers)
print('Разница между максимальным и минимальным значением дробной части элементов: ', max - min)
