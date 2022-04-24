import sys
from collections import deque

# global
N, M, T = 0, 0, 0
TRACE = True
DISHES = []
MOVES = []

def init():
    global N, M, T
    input = sys.stdin.readline
    N, M, T = map(int, input().rstrip().split())
    for _ in range(N):
        DISHES.append(deque(map(int, input().rstrip().split())))
    for _ in range(T):
        MOVES.append(list(map(int, input().rstrip().split())))

def rotates():
    for x, d, k in MOVES:
        rotate(x, d, k)
        if remove(): continue
        adjust()

def rotate(x, d, k):
    for i in range(N):
        if (i+1) % x != 0: continue
        for _ in range(k):
            if d == 0:
                DISHES[i].appendleft(DISHES[i].pop())
            else:
                DISHES[i].append(DISHES[i].popleft())
            
def remove():
    global TRACE
    not_adjust = False
    for i in range(N):
        for j in range(M):
            if DISHES[i][j] == -1: continue
            res = bfs(i, j, DISHES[i][j])
            not_adjust = not_adjust or res
    TRACE = not TRACE
    return not_adjust

def adjust():
    sum, n = 0, 0
    for i in range(N):
        for j in range(M):
            if DISHES[i][j] == -1: continue
            n, sum = n+1, sum+DISHES[i][j]

    if n == 0: return
    avg = sum / n
    for i in range(N):
        for j in range(M):
            v = DISHES[i][j]
            if v == -1 or v == avg: continue
            DISHES[i][j] += 1 if v < avg else -1
    

def bfs(i, j, v):
    Q = deque()
    Q.append((i, j))
    removed = False

    while Q:
        _i, _j = Q.popleft()

        for ni, nj in ((_i+1, _j), (_i-1, _j), (_i, _j+1), (_i, _j-1)):
            # nj 조정
            if nj == -1: nj = M-1
            elif nj == M: nj = 0

            # TRACE 및 값 일치 체크
            if ni == -1 or ni == N or DISHES[ni][nj] != v: continue

            # enqueue
            removed = True
            Q.append((ni, nj))
            DISHES[ni][nj] = -1
    if removed: DISHES[i][j] = -1
    return removed

def sum():
    res = 0
    for i in range(N):
        for j in range(M):
            if DISHES[i][j] == -1: continue
            res += DISHES[i][j]
    print(res)

# driver
init()
rotates()
sum()
