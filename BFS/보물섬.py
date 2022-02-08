# https://www.acmicpc.net/problem/2589

import sys
from collections import deque

def init():
    (ROW, COL), ROWS = sys.stdin.readline().split(), []
    ROW, COL = int(ROW), int(COL)
    for _ in range(ROW-1):
        ROWS.append(list(sys.stdin.readline())[:-1])
    ROWS.append(list(sys.stdin.readline()))
    return (ROW, COL, ROWS)

def answer(ROW, COL, graph):
    ans = 0
    for i in range(ROW):
        for j in range(COL):
            if graph[i][j] != 'W':
                ans = max(ans, bfs(i, j, ROW, COL, graph))
    return ans

def bfs(start_row, start_col, ROW, COL, graph):
    traced = [[data for data in row] for row in graph]
    Q = deque(((start_row, start_col, 0),))
    ans, traced[start_row][start_col] = 0, 'W'
    while Q:
        i, j, d = Q.pop()
        cases = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for (ni, nj) in cases:
            if ni in (-1, ROW) or nj in (-1, COL): continue
            if traced[ni][nj] == 'W': continue

            traced[ni][nj] = 'W'
            ans = max(ans, d+1)
            Q.appendleft((ni, nj, d+1))
    return ans

# driver
print(answer(*init()))