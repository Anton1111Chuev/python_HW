'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''
def by_number_system(number:int, basis:int = 16):
    result = []
    div = number
    dict = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14: 'e', 15: 'f'}
    while div >= basis:
        div, mode = divmod(div, basis)
        result.append(dict.get(mode, str(mode)))
    result.append(dict.get(div, str(div)))
    result.reverse()
    return ''.join(result)

num = int(input('Введите целое число для перевода в 16-ичную систему '))
print(f'Число в 16-ичной системе {by_number_system(num)}, контроль {hex(num)}')
