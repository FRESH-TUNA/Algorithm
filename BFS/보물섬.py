# https://www.acmicpc.net/problem/2589
import sys
from collections import deque

def init():
    ROW, COL = list(map(int, sys.stdin.readline().split()))
    GRAPH = []
    for _ in range(ROW): GRAPH.append(list(input()))
    return (ROW, COL, GRAPH)

def answer(ROW, COL, GRAPH):
    ans = 0
    for i in range(ROW):
        for j in range(COL):
            if GRAPH[i][j] == 'W': continue
            if i>0 and i+1 < ROW:
                if GRAPH[i-1][j] == "L" and GRAPH[i+1][j] == "L":
                    continue
            if j>0 and j+1 < COL:
                if GRAPH[i][j-1] == "L" and GRAPH[i][j+1] == "L":
                    continue
            ans = max(ans, bfs(i, j, ROW, COL, GRAPH))
    return ans

def bfs(start_row, start_col, ROW, COL, GRAPH):
    traced = [[0] * COL for _ in range(ROW)]
    Q = deque(((start_row, start_col),))
    ans, traced[start_row][start_col] = 0, 1
    while Q:
        i, j = Q.pop()
        cases = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for (ni, nj) in cases:
            if ni in (-1, ROW) or nj in (-1, COL): continue
            if traced[ni][nj] or GRAPH[ni][nj] == "W": continue
            traced[ni][nj] = traced[i][j]+1
            ans = max(ans, traced[ni][nj])
            Q.appendleft((ni, nj))
    return ans - 1
