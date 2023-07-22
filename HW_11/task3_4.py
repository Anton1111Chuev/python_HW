class Rectangle:
    """Class Rectangle
atr: length, width
methods: get_perimetp, get_square"""

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def get_perimetr(self):
        return (self.width + self.length) * 2

    def get_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        length = self.length - other.length
        width = self.width - other.width
        if length <= 0 or width <= 0:
            raise "invalid value"
        return Rectangle(length, width)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        return self.get_square() > other.get_square()

    def __repr__(self):
        return f'{self.length = } {self.width = }'

    def __str__(self):
        return f'Прямоугольник длина: {self.length}, ширина: {self.width}, периметр: {self.get_perimetr()}, площадь: {self.get_square()}'


