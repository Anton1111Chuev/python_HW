'''Создайте функцию генератор чисел Фибоначчи (см. Википедию)'''

def gen_fib_numbers(n: int):
    n_2, n_1 = 0, 1
    for i in range(0, n + 1):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            res = n_2 + n_1
            n_1, n_2 = res, n_1
            yield res

print(list(gen_fib_numbers(20)))

