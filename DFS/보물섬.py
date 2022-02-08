# https://www.acmicpc.net/problem/2589

from collections import deque

def init():
    ROW, COL = list(map(int, input().split()))
    ROWS = []
    while ROW:
        ROWS.append(list(input()))
        ROW -= 1
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
    ans = 0
    while Q:
        i, j, d = traced.pop()
        cases = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for (ni, nj) in cases:
            if ni in (-1, ROW) or nj in (-1, COL): continue
            if traced[ni][nj] == 'W': continue

            traced[ni][nj] = 'W'
            ans = max(ans, d+1)
            Q.appendleft((ni, nj, d+1))
    return ans


# driver
ROW, COL, graph = init()
print(answer(init()))
