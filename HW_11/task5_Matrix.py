class Matrix:
    """Matrix class.
Supports addition multiplication and equality checks"""

    def __init__(self,  max_line, max_column):
        self._max_column = max_column
        self._max_line = max_line
        self._matr = [[0 for i in range(max_column)] for j in range(max_line)]

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self._matr)

    def __getitem__(self, row_col: tuple):
        i, j = row_col
        self.__check_max(i, j)
        return self._matr[i][j]

    def __setitem__(self, key: tuple, value):
        i, j = key
        self.__check_max(i, j)
        self._matr[i][j] = value

    def __eq__(self, other):
        if self._max_column != other._max_column or self._max_line != other._max_line:
            return False
        for i, line in enumerate(self._matr):
            for j, value in enumerate(line):
                if value != other._matr[i][j]:
                    return False
        else:
            return True

    def __add__(self, other):
        if self._max_column != other._max_column or self._max_line != other._max_line:
            raise "sizes are different"
        res = Matrix(self._max_line, self._max_column)
        for i in range(self._max_line):
            for j in range(self._max_column):
                res[i, j] = self[i, j] + other[i, j]
        return res


    def __mul__(self, other):
        if self._max_column != other._max_line:
            raise "sizes  self line and other column are different"
        res = Matrix(self._max_line, other._max_column)
        for i in range(self._max_line):
            for j in  range(other._max_column):
                res[i, j] = sum(self[i, s] * other[s, j] for s in range(self._max_column))
        return res

    def __check_max(self, i, j):
        if i >= self._max_line   or j >= self._max_column:
            raise "index out of range"


a = Matrix(2, 3)
b = Matrix(3, 2)

a[0, 0] = 1
a[0, 1] = 2
a[0, 2] = 3
a[1, 0] = 4
a[1, 1] = 5
a[1, 2] = 6

b[0, 0] = 2
b[0, 1] = 2
b[1, 0] = 2
b[1, 1] = 2
b[2, 0] = 2
b[2, 1] = 2

print(a)
print('\n')
print(b)
print('\n')
print(a * b)