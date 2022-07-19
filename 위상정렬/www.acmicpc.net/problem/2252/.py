import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
G, W = defaultdict(list), [0] * (N + 1)
ANS, Q = [], deque()

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    W[b] += 1

for i in range(1, N + 1):
    if W[i] == 0: Q.append(i)
            
while Q:
    node = Q.popleft()
    ANS.append(node)
    for v in G[node]:
        W[v] -= 1 
        if W[v] == 0: Q.append(v)

print(*ANS)
