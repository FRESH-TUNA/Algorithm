from sys import stdin
from collections import deque

input = stdin.readline
dr, dc, D = (-1, 0, 1, 0), (0, -1, 0, 1), 4

row, column = map(int, input().split())
lake, swan = [], []
water = deque()

def find_swan(lake, visited, queue):
    next_queue = deque()
    while queue:
        r, c = queue.popleft()
        if r == swan[1][0] and c == swan[1][1]:
            return True, None
        
        for d in range(D):
            nr = r + dr[d]
            nc = c + dc[d]
            if not 0 <= nr < row or not 0 <= nc < column:
                continue
            if visited[nr][nc]:
                continue
            if lake[nr][nc] == 'X':
                next_queue.append((nr, nc))
            else:
                queue.append((nr, nc))
            visited[nr][nc] = True

    return False, next_queue

def melt_ice(water, lake):
    next_water = deque()
    while water:
        r, c = water.popleft()
        for d in range(D):
            nr = r + dr[d]
            nc = c + dc[d]
            if not 0 <= nr < row or not 0 <= nc < column:
                continue
            if lake[nr][nc] == 'X':
                next_water.append((nr, nc))
                lake[nr][nc] = '.'
    
    return next_water


def init():
    for r in range(row):
        current_lake_info = list(input().rstrip())
        for c, v in enumerate(current_lake_info):
            if v == '.' or v == 'L':
                water.append((r, c))
            if v == 'L':
                swan.append((r, c))
        lake.append(current_lake_info)

def call():
    global water, queue
    
    day = -1
    visited = [[0 for _ in range(column)] for _ in range(row)]
    queue = deque()

    r, c = swan[0]
    queue.append((r, c))
    visited[r][c] = 1

    while True:
        day += 1
        found, next_queue = find_swan(lake, visited, queue)
        if found:
            break
        water, queue = melt_ice(water, lake), next_queue
    print(day)
    
init()
call()

