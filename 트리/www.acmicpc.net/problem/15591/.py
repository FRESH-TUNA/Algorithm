import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G, D = [[] for _ in range(N+1)], [[0]*(N+1) for _ in range(N+1)]
    
    def tree():
        for _ in range(N-1):
            p, q, r = map(int, input().split())
            G[p].append(q)
            G[q].append(p)
            D[p][q] = D[q][p] = r

    tree()
    print(G)
solution()
