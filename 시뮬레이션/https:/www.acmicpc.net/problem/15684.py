import sys

# global
res = sys.maxsize

#https://suri78.tistory.com/212

def solution(N, M, H, ladder):
    for d in range(4):
        dfs(N, ladder, 0, 0, r)
        if res != sys.maxsize: return res
    return -1

def dfs(N, ladder, cnt, i, r):
    if cnt == r:
        if move(): res = cnt
        return

    for i in range(idx, h):
        for j in range(N):
            if ladder[j][i]: continue
            if j-1 >= 0 and ladder[j-1][i]: continue
            if j+1 < N and ladder[j+1][i]
            ladder[j][i] = 1
            dfs(cnt+1, i, r)
            ladder[j][i] = 0

# driver
input = sys.stdin.readline
N, M, H = map(int, input.split())

# 각 세로선당 가로선
ladder = [[0]*(H+1) for _ in range(N+1)]
for _ in range(M):
    # 가로선 / 세로선
    x, y = map(int, input().split())
    ladder[y][x] = 1
print(solution(N, M, H, ladder))