import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
G, T = [[] for _ in range(N+1)], [0 for _ in range(N+1)]

def graph():
    for _ in range(M):
        start, end = map(int, input().split())
        G[start].append(end)

def call():
    target, q = 0, deque()
    q.append(X)
    T[X] = 1

    while q:
        if target == K:
            return '\n'.join(str(node) for node in sorted(q))

        target += 1
        for _ in range(len(q)):
            node = q.popleft()
            for new_node in G[node]:
                if not T[new_node]:
                    T[new_node] = 1
                    q.append(new_node)
    return -1

graph()
print(call())
