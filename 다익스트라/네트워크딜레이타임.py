class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        checked, dists = set(), [100000000] * (n+1)
        dists[k], queue = 0, [(0, k)]
        graph = [[] for _ in range(n+1)]  
        
        for (i, j, dist) in times: graph[i].append((dist, j))
        
        while queue:
            dist, node = heapq.heappop(queue)
            
            if node in checked: continue
            else: checked.add(node)
            
            for (_dist, end) in graph[node]:
                if dist + _dist < dists[end]:
                    dists[end] = dist + _dist
                    heapq.heappush(queue, (dists[end], end))
        
        ans = max(dists[1:])
        return -1 if ans == 100000000 else ans
