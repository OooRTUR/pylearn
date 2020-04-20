from  random import  randint

class LineChecker():
    @staticmethod
    def checkLineIdent(line):
        firsItem = line[0]
        if firsItem == '-': return False
        for i in range(1,len(line)):
            if firsItem != line[i]:
                return False
        return True
    @staticmethod
    def checkDiagonalIdent(matrix):

        firsItem = matrix[0][0]
        if firsItem == '-': return False
        for i in range(1,len(matrix)):
            if firsItem != matrix[i][i]:
                return  False
        return True

    def checkDiagonalIdent1(matrix):
        firsItem = matrix[len(matrix) - 1][len(matrix) - 1]
        if firsItem == '-': return False
        for i in range(1, len(matrix)):
            if firsItem != matrix[i][len(matrix) - 1 - i]: return False
        return  True

def out_field():
    print('out')
    for i in range(3):
        for j in range(3):
            print(field[i][j],end=' ')
        print()


def input_coord(var_name):
    res = None
    while True:
        res = int(input(f'Введите координату {var_name}: '))
        if res <=3 and res >=1:
            break
    return  res

def check_is_cell_available(x,y):
    return field[y-1][x-1] == '-'

def check_is_any_available_cell():
    for i in range(len(field)):
        for j in range(i):
            if field[i][j] == '-': return True
    return  False

def enemy_turn():
    if(check_end()): return True

    while True:
        x = randint(1,3)
        y = randint(1,3)
        if check_is_cell_available(x,y):
            field[y-1][x-1] ='o'
            break
    return  check_end()



def check_end():
    if LineChecker.checkDiagonalIdent(field): return  True
    if LineChecker.checkDiagonalIdent1(field): return True
    for line in field:
        print(line)
        if LineChecker.checkLineIdent(line): return True
    for i in range(len(field)):
        row = [row[i] for row in field]
        if LineChecker.checkLineIdent(row): return True
    return not check_is_any_available_cell()


def finish_game():
    print('finish game')

field = [['-','-','-'],['-','-','-'],['-','-','-']]
# field =[[1,2,3],[4,5,6],[7,8,9]]
out_field()

game_over = False
while not game_over:
    x =input_coord('x')
    y =input_coord('y')

    if(check_is_cell_available(x,y)):
        field[y-1][x-1] = 'x'
    else:
        print('cell is not available')
        continue

    game_over = enemy_turn()

    out_field()

finish_game()