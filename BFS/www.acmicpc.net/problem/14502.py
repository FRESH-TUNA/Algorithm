import sys, copy
from itertools import combinations, product
from collections import deque

def solution(N, M, g):
    VS = find_viruss(N, M, g)
    MAX_ANS = get_max_ans(N, M, g)
    CASES = combinations(product(range(N), range(M)), 3)
    ans = 0

    for ((x1, y1), (x2, y2), (x3, y3)) in CASES:
        if g[x1][y1] or g[x2][y2] or g[x3][y3]: 
            continue
        g[x1][y1], g[x2][y2], g[x3][y3] = 1, 1, 1
        traced, new_ans = copy.deepcopy(g), MAX_ANS
        for (vx, vy) in VS: 
            new_ans -= bfs(N, M, vx, vy, traced)
            if new_ans <= ans: break
        ans = max(ans, new_ans)
        g[x1][y1], g[x2][y2], g[x3][y3] = 0, 0, 0
    return ans

def bfs(N, M, x, y, traced):
    Q, ans = deque(), 0
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()
        nxys = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        for (nx, ny) in nxys:
            if nx in (-1, N) or ny in (-1, M) or traced[nx][ny]: 
                continue
            ans += 1
            traced[nx][ny] = 1
            Q.append((nx, ny))
    return ans

def find_viruss(N, M, graph):
    xys = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                xys.append((i, j))
    return xys

def get_max_ans(N, M, graph):
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                ans += 1
    return ans - 3

# driver
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [ list(map(int, input().split()[:M])) 
          for _ in range(N) ]
print(solution(N, M, graph))
