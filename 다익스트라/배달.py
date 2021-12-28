import heapq

def solution(N, road, K):
    dists, dists[1] = [10000000 for _ in range(N + 1)], 0
    is_traced = set()
    graph, queue = [[] for _ in range(N + 1)], [(0, 1)]
    
    for (i, j, d) in road:
        graph[i].append((j, d))
        graph[j].append((i, d))

    while queue:
        v_dist, v = heapq.heappop(queue)

        if v in is_traced: continue
            
        is_traced.add(v)

        for (dest, dist) in graph[v]:
            candid_dist = v_dist + dist
            if candid_dist < dists[dest]:
                dists[dest] = candid_dist
                heapq.heappush(queue, (candid_dist, dest))
    
    return len(list(filter(lambda d: d <= K, dists)))
