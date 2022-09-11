from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]
DB = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i!=0:
            DB[i][j] = DB[i-1][j]
        if j!=0:
            DB[i][j] = max(DB[i][j], DB[i][j-1])
        DB[i][j] += G[i][j] 
print(DB[-1][-1])

