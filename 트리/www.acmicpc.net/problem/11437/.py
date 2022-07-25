import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N+1)]
    P, D = [0]*(N+1), [0]*(N+1)
    ROOT = 1
    
    def graph():
        for _ in range(N-1):
            a, b = map(int, input().split())
            G[a].append(b)
            G[b].append(a)

    def parent():
        q, depth = deque(), 0
        q.append(ROOT)
        P[ROOT], D[ROOT] = 1, depth

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                for child in G[node]:
                    if child != P[node]:
                        P[child], D[child] = node, depth
                        q.append(child)

    def calculate(a, b):
        while D[a] != D[b]:
            if D[a] > D[b]:
                a = P[a]
            else:
                b = P[b]

        while a != b:
            a, b = P[a], P[b]
        return a

    def calculates():
        answer = []
        for _ in range(int(input())):
            a, b = map(int, input().split())
            answer.append(calculate(a, b))
        print(*answer, sep="\n")
            
    graph()
    parent()
    calculates()
    
solution()

