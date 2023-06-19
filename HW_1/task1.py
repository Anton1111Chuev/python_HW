'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''


def is_triangle(a: int, b: int, c: int) -> {str, str | bool}:
    result = {'isTriangle': False, 'descpiption': "Введеные значения длин не подходят для треугольника"}

    result['isTriangle'] = ((a + b) >= c and (a + c) >= b and (b +c) >= a)

    if not result['isTriangle']:
        return result

    equilateralTriangle = (a == b == c)
    isoscelesTriangle = (a == b or a == c or b == c)

    result['descpiption'] = f'Треугольник равносторонний {equilateralTriangle}, треугольник равнобедренный = {isoscelesTriangle}'

    return result

a = int(input('введите сторону а треугольника '))
b = int(input('введите сторону b треугольника '))
c = int(input('введите сторону c треугольника '))

res = is_triangle(a, b, c)
for key, value in res.items():
    print(f'{key = } {value=}')