import sys

N = 9
sudoku = [[int(c) for c in sys.stdin.readline().rstrip()] for _ in range(N)]
row = [[0]*(N+1) for _ in range(N)]
col = [[0]*(N+1) for _ in range(N)]
square = [[0]*(N+1) for _ in range(N)]

def init():
    for r in range(N):
        for c in range(N):
            v = sudoku[r][c]
            row[r][v] = col[c][v] = square[r//3*3+c//3][v] = 1

def solve(r, c):
    if r==9:
        return True

    nc = (c+1)%N
    nr = r+1 if nc==0 else r

    if sudoku[r][c]:
        return solve(nr, nc)
    else:
        for v in range(N+1):
            if not (row[r][v] or col[c][v] or square[r//3*3+c//3][v]):
                row[r][v] = col[c][v] = square[r//3*3+c//3][v] = 1
                sudoku[r][c] = v
                if solve(nr, nc):
                    return True
                row[r][v] = col[c][v] = square[r//3*3+c//3][v] = 0
                sudoku[r][c] = 0
        return False
    

# driver
init()
solve(0, 0)
print('\n'.join(''.join(str(c) for c in row) for row in sudoku))

