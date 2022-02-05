import heapq

MAX_NODES = 200
MAX_FARE = 100000

def solution(n, s, a, b, fares):
    graph = init_graph(fares)
    dists = [[MAX_NODES * MAX_FARE 
             for _ in range(MAX_NODES+1)] 
             for _ in range(MAX_NODES+1)]
    calculate_dists(graph, dists, n)
    return answer(dists, n, s, a, b)

def init_graph(fares):
    graph = [dict() for _ in range(MAX_NODES + 1)]
    
    for start, end, fare in fares:
        graph[end][start] = graph[start][end] = fare
    return graph

def calculate_dists(graph, dists, n):
    for root in range(1, n+1):
        calculate_dist(graph, dists, root)
    
def calculate_dist(graph, dists, root):
    dists[root][root] = 0
    Q = [(0, root)]
    
    while Q:
        dist, start = heapq.heappop(Q)
        for end in graph[start]:
            _dist = graph[start][end]
            if dists[root][end] > _dist + dist:
                dists[root][end] = _dist + dist
                heapq.heappush(Q, (_dist + dist, end))
                
            
def answer(dists, n, start, dist_a, dist_b):
    ans = dists[start][dist_a] + dists[start][dist_b]

    for sub_dist in range(1, n+1):
        ans = min(ans, dists[start][sub_dist] + 
                  dists[sub_dist][dist_a] + 
                  dists[sub_dist][dist_b])
    return ans