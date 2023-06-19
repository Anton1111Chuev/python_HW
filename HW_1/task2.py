'''3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'''

def is_prime_number(number):

    if not isinstance(number, int) or number < 0 or number > 100000:
        print("Необходимо ввести целое число от 1 до 100000")
        return False

    if number in (0, 1, 2):
        return True

    max_value = number
    pos = 2
    while pos < max_value:
        if number % pos == 0:
            return False
        max_value = int(round(number/pos) + 1)
        pos += 1

    return True

number = int(input('Введите число от 0 до 100000 для проверки на простоту '))
print(f'Результат проверки числа {number} на простоту: {is_prime_number(number)}')
