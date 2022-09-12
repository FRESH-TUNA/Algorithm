import sys

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
DB = [[0]*N for _ in range(N)]
D, DR, DC = 4, (-1,0,1,0), (0,1,0,-1)

def dfs(i, j):
    max_value = 0
    for d in range(D):
        ni, nj = i+DR[d], j+DC[d]
        if ni==-1 or ni==N or nj==-1 or nj==N or G[ni][nj]<=G[i][j]:
            continue
        if not DB[ni][nj]:
            dfs(ni, nj)
        max_value = max(max_value, DB[ni][nj])
    DB[i][j] = 1+max_value

def answer():
    sys.setrecursionlimit(30000)
    for i in range(N):
        for j in range(N):
            if not DB[i][j]:
                dfs(i, j)
    print(max(max(row) for row in DB))
    
answer()
