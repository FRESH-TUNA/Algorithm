import sys
from collections import deque

# global static
N = 101
DI, DJ = (0, -1, 0, 1), (1, 0, -1, 0)

def solution(cows):
    graph = [[0] * N for _ in range(N)]
    for cow in cows: add_cow(graph, *cow)
    return squares(graph)

def add_cow(graph, j, i, d, g):
    Q = deque(((i+DI[d], j+DJ[d]), (i, j)))
    for x in range(g):
        ai, aj = Q[0][0] * (-1), Q[0][1] * (-1)
        NQ = deque()
        for i in range(1, 2**x + 1):
            ti, tj = Q[i][1]+aj-ai, (Q[i][0]+ai) * (-1)-aj
            NQ.append((ti, tj))
        Q.extendleft(NQ)
    for (i, j) in Q: graph[i][j] = 1

def squares(g):
    res = 0
    for i in range(N-1):
        for j in range(N-1):
            if g[i][j] & g[i+1][j] & g[i][j+1] & g[i+1][j+1]:
                res += 1
    return res

# driver
input = sys.stdin.readline
n = int(input())
cows = [list(map(int, input().split()[:4]))
        for _ in range(n)]
print(solution(cows))
