import sys, heapq
from collections import defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())
MAX_TIME, MAX_DIST = 1000000*10000, 1000000
DISTS = [defaultdict(lambda: MAX_DIST) for _ in range(N+1)]
G = [[] for _ in range(N+1)]
DB = [[MAX_TIME]*(K+1) for _ in range(N+1)]

def graph():
    for _ in range(M):
        a, b, d = map(int, input().split())
        DISTS[a][b] = DISTS[b][a] = min(DISTS[b][a], d)
        G[a].append(b); G[b].append(a);

def call():
    q = []
    DB[1] = [0]*(K+1)
    
    heapq.heappush(q, (0,1,0))

    while q:
        dist, node, k = heapq.heappop(q)
        
        if DB[node][k] < dist:
            continue
            
        for new_node in G[node]:
            if dist+DISTS[node][new_node] < DB[new_node][k]:
                DB[new_node][k] = dist+DISTS[node][new_node]
                heapq.heappush(q, (DB[new_node][k], new_node, k))

            if k < K and dist < DB[new_node][k+1]:
                DB[new_node][k+1] = dist
                heapq.heappush(q, (dist, new_node, k+1))
    print(min(DB[-1]))

graph()
call()

