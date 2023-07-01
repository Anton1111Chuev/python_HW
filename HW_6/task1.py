from random import randint
SIZE = 8
count = 0
chess_board = [[0 for i in range(SIZE)] for j in range(SIZE)]
answer = []
def action_with_queen(i, j, action = 1):
    for z in range(SIZE):
        chess_board[z][j] += action
        chess_board[i][z] += action
        if 0 <= i + j - z < SIZE:
            chess_board[i + j - z][z] += action
        if 0 <= i - j + z < SIZE:
            chess_board[i - j + z][z] += action
    chess_board[i][j] = -1 if action == 1 else 0

def print_answer():
    global count
    ans = set()
    for i in range(SIZE):
        for j in range(SIZE):
            if chess_board[i][j] == -1:
                ans.add((i, j))
    answer.append(ans)
    print(ans)
    count += 1

def find_position_recursive(i):
    '''рекурсивно генерирует все возможный ответы (в списке chess_board i, j = -1)'''
    for j in range(SIZE):
        if chess_board[i][j] == 0:
            action_with_queen(i, j)
            if i == SIZE - 1:
                print_answer()
            else:
                find_position_recursive(i + 1)
            action_with_queen(i, j, -1)

def rand_position():
    '''Создает рандомно расстановку (т.е вариаант ответа для проверки) - множество кортежей'''
    res = set()
    while len(res) < SIZE:
        res.add((randint(0, SIZE - 1), randint(0, SIZE - 1)))
    return res

def test_position(position: set) -> bool:
    '''проверяет по переданному множеству соотвествует ли оно одному из корректных ответов'''
    return position in answer

find_position_recursive(0)
print(f'Всего верных ответов: {count}')

count_try_ramdom = 0
right_try = 0

'''Сами ответы генерируются за несколько секунд - естественно вызов рандома и проверка работает долго, в среднем 35 млн вариантов до одного правильного'''
while right_try < 4:
    position = rand_position()
    count_try_ramdom += 1
    if test_position(position):
        right_try += 1
        print(f'Верно сгенерирован вариант: {position} \nВсего попыток: {count_try_ramdom}')