from collections import deque
import sys

APPLE, TRACE = 2, 1

# 사과는 2
def solution(N, graph, apples, turns):
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    d, time = 0, 0
    traced = deque()
    traced.append((0, 0))

    while True:
        time += 1
        r, c = traced[-1]
        nr, nc = ds[d][0]+r, ds[d][1]+c
    
        if nr in (-1, N) or nc in (-1, N) or graph[nr][nc] == 1:
            return time
    
        traced.append((nr, nc))
        if graph[nr][nc] != APPLE: traced.popleft()
        graph[nr][nc] = 1

        if turns and turns[0][0] == time:
            nd = turns.popleft()[1]
            if nd == 'D': d = (d+1) % 4
            else: d = 3 if d-1 == -1 else d-1

# driver
input = sys.stdin.readline
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

APPLES_N = int(input())
apples = [list(map(int, input().split())) for _ in range(APPLES_N)]
for (r, c) in apples: graph[r][c] = APPLE
    
TURNS_N = int(input())
turns = deque()
for _ in range(TURNS_N):
    turn = input().split()
    turns.append((int(turn[0]), turn[1]))

print(solution(N, graph, apples, turns))
