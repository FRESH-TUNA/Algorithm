from collections import deque

def solution(m, n, board):
    answer = 0
    while True:
        punged_amount, board = pung(m, n, board)
        if punged_amount == 0: return answer
        answer += punged_amount
        board = shift(board)

def pung(m, n, board):
    ans, new_board = 0, [[d for d in r] for r in board]
    for i in range(m):
        for j in range(n):
            if board[i][j] == "X": new_board[i][j] = "X"
            else: ans += pung_idx(m, n, board, i, j, new_board)
    return ans, new_board

def pung_idx(m, n, board, i, j, new_board):
    ans = 0
    cases = (((-1, 0), (-1, 1), (0, 1)), ((0, 1), (1, 1), (1, 0)),
             ((1, 0), (1, -1), (0, -1)), ((0, -1), (-1, -1), (-1, 0)))    
    for case in cases:
        if pungable(m, n, board, i, j, case): ans += pung_case(i, j, case, new_board)
    return ans

def pungable(m, n, board, i, j, case):
    for (_x, _y) in case:
        c_x, c_y = _x + i, _y + j
        if not c_x in range(m) or not c_y in range(n) or \
           board[i][j] != board[c_x][c_y]: return False
    return True

def pung_case(i, j, case, new_board):
    ans = 0
    for (_x, _y) in list(case) + [(0, 0)]:
        if new_board[_x + i][_y + j] != "X":
            new_board[_x + i][_y + j] = "X"
            ans += 1
    return ans

def shift(board):
    columns = list(zip(*board))
    for idx, column in enumerate(columns):
        new_column = deque()
        for block in column:
            if block == "X": new_column.appendleft(block)
            else: new_column.append(block)
        columns[idx] = list(new_column)
    return list(zip(*columns))
