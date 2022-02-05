import heapq

MAX_NODES = 200
MAX_FARE = 100000

def solution(n, s, a, b, fares):
    dists = [[MAX_NODES * MAX_FARE 
             for _ in range(MAX_NODES+1)] 
             for _ in range(MAX_NODES+1)]
    init_dists(fares, dists, n)
    calculate_dists(fares, dists, n)
    return answer(dists, n, s, a, b)

def init_dists(fares, dists, n):
    for start, end, fare in fares:
        dists[end][start] = dists[start][end] = fare
    for node in range(1, n+1): dists[node][node] = 0
        
def calculate_dists(fares, dists, n):
    for node in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                _dist = dists[start][node] + dists[node][end]
                if dists[start][end] > _dist:
                    dists[start][end] = _dist
            
def answer(dists, n, start, dist_a, dist_b):
    ans = dists[start][dist_a] + dists[start][dist_b]

    for sub_dist in range(1, n+1):
        ans = min(ans, dists[start][sub_dist] + 
                  dists[sub_dist][dist_a] + 
                  dists[sub_dist][dist_b])
    return ans
