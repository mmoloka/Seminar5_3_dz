# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
numbers = list()
count = 0

while n >= 2:
    numbers.append(n - ((n // 2) * 2))
    n = n // 2
    count += 1
numbers.append(n)

bin_number = ''
for i in range(count + 1):
    bin_number += str(numbers[-1-i])

print('Двоичный вид числа: ', bin_number)
