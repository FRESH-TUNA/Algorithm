from collections import deque

def solution(maps):
    row_num, col_num = len(maps), len(maps[0])
    last_row, last_col = row_num - 1, col_num - 1
    queue = deque([[0, 0, 1]]) 
    is_traced = [[False for _ in range(col_num)] for _ in range(row_num)]
    is_traced[0][0] = True
    
    while queue:
        x, y, d = queue.pop()

        # destination ?
        if x == last_row and y == last_col: return d

        # cases filtering
        new_cases = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
        for (_x, _y) in new_cases:
            if _x not in range(row_num) or _y not in range(col_num): continue
            if maps[_x][_y] == 0 or is_traced[_x][_y]: continue
            is_traced[_x][_y] = True
            queue.appendleft([_x, _y, d + 1])

    return (-1)
