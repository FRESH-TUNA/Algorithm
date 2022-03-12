import sys, copy
from itertools import product

# global static
NO, EA, SO, WE = 0, 1, 2, 3
TRACE_INFOS = (
    ((), (NO,), (NO, SO), (NO, EA), (WE, NO, EA), (NO, EA, SO, WE)),
    ((), (EA,), (EA, WE), (EA, SO), (NO, EA, SO), (NO, EA, SO, WE)),
    ((), (SO,), (SO, NO), (SO, WE), (EA, SO, WE), (NO, EA, SO, WE)),
    ((), (WE,), (WE, EA), (WE, NO), (SO, WE, NO), (NO, EA, SO, WE)),
)
MDS = ((-1, 0), (0, 1), (1, 0), (0, -1))
VISITED = 7

def solution(N, M, GRAPH):
    CCTVS = get_cctv_infos(N, M, GRAPH)
    CASES = product((NO, EA, SO, WE), repeat = len(CCTVS))
    traced_n = 0

    for c in CASES:
        c_traced_n = cctv_check(N, M, CCTVS, copy.deepcopy(GRAPH), c)
        if c_traced_n > traced_n: traced_n = c_traced_n
    return get_max_traces_n(N, M, GRAPH) - traced_n
    
def cctv_check(N, M, CCTVS, traced, case):
    res = 0
    for (i, j, t), d in zip(CCTVS, case):
        res += trace(N, M, traced, i, j, TRACE_INFOS[d][t])
    return res

def trace(N, M, traced, i, j, TRACE_INFO):
    res = 0
    for t in TRACE_INFO:
        ni, nj = i, j
        while True:
            ni, nj = MDS[t][0]+ni, MDS[t][1]+nj
            if ni in (N, -1) or nj in (M, -1):
                break
            if not(not traced[ni][nj] or traced[ni][nj] == VISITED): 
                break
            if traced[ni][nj] != VISITED: 
                traced[ni][nj], res = VISITED, res+1
    return res

def get_cctv_infos(N, M, GRAPH):
    res = []
    for i in range(N):
        for j in range(M):
            if GRAPH[i][j] not in (0, 6):
                res.append((i, j, GRAPH[i][j]))
    return res

def get_max_traces_n(N, M, GRAPH):
    res = 0
    for i in range(N):
        for j in range(M):
            if not GRAPH[i][j]: res += 1
    return res
    
# driver
input = sys.stdin.readline
N, M = map(int, input().split())
GRAPH = [list(map(int, input().split()[:M])) for _ in range(N)]
print(solution(N, M, GRAPH))
