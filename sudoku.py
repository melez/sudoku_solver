sudoku = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

sudoku = [
        [0, 0, 0, 0, 1, 0, 0, 5, 0],
        [0, 7, 0, 0, 3, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 9, 2, 0, 0],
        [0, 5, 8, 0, 0, 1, 0, 0, 3],
        [0, 0, 2, 6, 0, 8, 5, 0, 0],
        [4, 0, 0, 5, 0, 0, 9, 2, 0],
        [0, 0, 9, 1, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 6, 0, 0, 7, 0],
        [0, 6, 0, 0, 5, 0, 0, 0, 0],
]

def check_board(b):
    for x in range(len(b)):
        for y in range(len(b[x])):
            if not str(b[x][y]).isdigit():
                b[x][y]=0
            else:
                b[x][y]=int(b[x][y])


def empty_cell(b):
    for x in range(len(b)):
        for y in range(len(b[x])):
            if not (b[x][y]>=1 and b[x][y]<=9):
                return x,y
    return None

def valid(b,num,x,y):
    for col in range(len(b[x])):
        if b[x][col]==num:
            return False
    for row in range(len(b[y])):
        if b[row][y]==num:
            return False    
    for col in range(x//3*3,x//3*3+3):
        for row in range(y//3*3,y//3*3+3):
            if b[col][row]==num:
                return False
    return True

def solve(b):
    check_board(b)
    if not empty_cell(b):
        return True
    else:
        x,y = empty_cell(b)
    for number in range(1,10):
        if valid(b,number,x,y):
            b[x][y] = number
            if solve(b):
                return True
            b[x][y] = 0
    return False

def show(b):
    line=""
    for x in range(len(b)):
        for y in range(len(b[x])):
            line+=str(b[x][y])
            if((y+1)%3==0):
                line+="|"
        if((x+1)%3==0):
            line+="\n"+"-"*(len(line))    
        print(line)
        line=""

show(sudoku)
solve(sudoku)
show(sudoku)
