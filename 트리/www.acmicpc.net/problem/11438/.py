import sys
from collections import deque
from math import log2

def solution():
    input = sys.stdin.readline
    N, ROOT = int(input()), 1
    G, NP = [[] for _ in range(N+1)], int(log2(N))+1
    P, D = [[0 for _ in range(NP+1)] for _ in range(N+1)], [0]*(N+1)

    def graph():
        for _ in range(N-1):
            a, b = map(int, input().split())
            G[a].append(b)
            G[b].append(a)

    def parent():
        q, depth, traced = deque(), 1, [0]*(N+1)
        
        q.append(ROOT)
        P[ROOT][0], D[ROOT], traced[ROOT] = ROOT, 0, 1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for child in G[node]:
                    if not traced[child]:
                        q.append(child)
                        P[child][0], D[child], traced[child] = node, depth, 1
            depth += 1 

    def grand_parent():
        for i in range(1, NP+1):
            for j in range(1, N+1):
                P[j][i] = P[P[j][i-1]][i-1]

    def lca(a, b):
        if D[a] > D[b]:
            a, b = b, a

        for i in range(NP-1, -1, -1):
            if D[b] - D[a] >= (1 << i):
                b = P[b][i]

        if a == b:
            return a

        for i in range(NP-1, -1, -1):
            if P[a][i] != P[b][i]:
                a = P[a][i]
                b = P[b][i]
        return P[a][0]

    def call():
        for _ in range(int(input())):
            print(lca(*(map(int, input().split()))))
    
    graph()
    parent()
    grand_parent()
    call()
solution()

