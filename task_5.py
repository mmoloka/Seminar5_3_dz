# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def empty_list(len):
    list = []
    for i in range(len):
        list.append(0)
    return list


n = int(input('Введите число: '))

fib = empty_list(n+1)
fib[1] = 1
for i in range(2, n+1):
    fib[i] = fib[i - 1] + fib[i - 2]

negafib = empty_list(n)
negafib[-1] = 1
negafib [-2] = -1
for j in range(2, n):
    negafib[-j-1] = negafib[-j+1] - negafib[-j]

print('Список Фибоначчи: \n', negafib + fib)
