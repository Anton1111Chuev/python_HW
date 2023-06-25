'''Напишите функцию для транспонирования матрицы'''
def trans_matrix(lst:list[list]):
    row = zip(*lst)
    return [list(r) for r in row]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(trans_matrix(matrix))