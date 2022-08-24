import sys
from collections import defaultdict
import heapq

# init
MAX_DIST, START = 10_000_000, 1
input = sys.stdin.readline
T = int(input())
N, M, K = [0]*T, [0]*T, [0]*T
E = [None]*T
for i in range(T):
    N[i], M[i], K[i] = map(int, input().split())
    E[i] = [list(map(int, input().split())) for _ in range(K[i])]

# solution
def solution(t):
    n, m, k, edges = N[t], M[t], K[t], E[t]
    G, Q = defaultdict(list), []
    dists = [[MAX_DIST]*(m+1) for _ in range(n+1)] 
    
    # graph init
    for i, j, c, d in edges:
        G[i].append([j, c, d])
    
    dists[START][0] = 0
    heapq.heappush(Q, (0, 0, START))

    while Q:
        s_dist, s_cost, s = heapq.heappop(Q)
        #if s_dist > dists[s][s_cost]: continue
            
        for end, cost, dist in G[s]:
            if s_cost + cost > m: continue
            n_cost = s_cost + cost
            n_dist = dists[s][s_cost] + dist
            if dists[end][n_cost] > n_dist:
                for c in range(n_cost, m+1):
                    if dists[end][c] < n_dist:
                        break
                    else:
                        dists[end][c] = n_dist
                dists[end][n_cost] = n_dist
                heapq.heappush(Q, (dists[end][n_cost], n_cost, end))
    res = min(dists[-1])
    return [str(res), "Poor KCM"][res == MAX_DIST]

# driver
print('\n'.join(solution(t) for t in range(T)))
