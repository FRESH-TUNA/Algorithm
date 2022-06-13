import sys

# global
ans = 0

def solution(N, M, graph):
    global ans
    traced = [[0 for j in range(M)] for i in range(N)]
    max_val = max(map(max, graph))

    for i in range(N):
        for j in range(M):
            block_check(graph, i, j, N, M)
            traced[i][j] = 1
            dfs(N, M, i, j, graph, traced, graph[i][j], 1, max_val)
            traced[i][j] = 0
    return ans

def block_check(graph, i, j, N, M):
    global ans
    cases = (
        ((i-1, j), (i, j-1), (i, j+1)),
        ((i+1, j), (i, j-1), (i, j+1)),
        ((i, j-1), (i+1, j), (i-1, j)),
        ((i, j+1), (i+1, j), (i-1, j))
    )
    for case in cases:
        _ans, valid = graph[i][j], True
        
        for (ni, nj) in case:
            if ni in (-1, N) or nj in (-1, M):
                valid = False
                break
            else: _ans += graph[ni][nj]

        if valid: ans = max(ans, _ans)

def dfs(N, M, i, j, graph, traced, agg, depth, max_val):
    global ans

    if depth == 4:
        ans = max(ans, agg)
        return

    if max_val * (4-depth) + agg <= ans:
        return

    cases = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
    for (ni, nj) in cases:
        if ni in (-1, N) or nj in (-1, M): continue
        if traced[ni][nj]: continue

        traced[ni][nj] = 1
        dfs(N, M, ni, nj, graph, traced, 
            agg + graph[ni][nj], depth+1, max_val)
        traced[ni][nj] = 0

# driver
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split()[:M])) for _ in range(N)]
print(solution(N, M, graph))