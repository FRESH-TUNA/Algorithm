import sys
from collections import deque

# global
REMOVED, GRAPH = [], []
TRACED, TRACE = [], True
N, M = 0, 0
BN, BM = 0, 0

def init():
    global REMOVED, GRAPH, TRACED, TRACE, N, M, BN, BM
    input = sys.stdin.readline
    N, M = map(int, input().split())
    BN, BM = {-1, N}, {-1, M}
    REMOVED = [[0]*M for _ in range(N)]
    TRACED = [[False]*M for _ in range(N)]
    GRAPH = [list(map(int, input().rstrip().split())) for _ in range(N)]

def solution():
    res = 0
    while True:
        lands, blocks = land_info()
        if lands >= 2: return res
        elif not blocks: return 0
        remove()
        res += 1
    return res

def remove():
    for i in range(N):
        for j in range(M):
            if not GRAPH[i][j]: continue
            for ai, aj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if ai in BN or aj in BM: continue
                if GRAPH[ai][aj] <= 0: REMOVED[i][j] += 1

    for i in range(N):
        for j in range(M):
            if REMOVED[i][j]:
                REMOVED[i][j], GRAPH[i][j] = 0, GRAPH[i][j] - REMOVED[i][j]

def land_info():
    global TRACE
    lands, blocks = 0, 0
    for i in range(N):
        for j in range(M):
            if GRAPH[i][j] <= 0 or TRACED[i][j] == TRACE: continue
            lands += 1
            if lands == 2: return lands, blocks 
            blocks += bfs(i, j)
    TRACE = not TRACE
    return lands, blocks

def bfs(i, j):
    Q = deque()
    Q.append((i, j)); 
    TRACED[i][j], res = TRACE, 1;

    while Q:
        i, j = Q.popleft()
        for ai, aj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if ai in BN or aj in BM: continue
            if GRAPH[ai][aj] <= 0 or TRACED[ai][aj] == TRACE: continue
            res += 1
            TRACED[ai][aj] = TRACE
            Q.append((ai, aj))
    return res

init()
print(solution())
