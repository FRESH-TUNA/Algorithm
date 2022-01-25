class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = collections.defaultdict(dict)
        graph = collections.defaultdict(dict)
        Q = [(0, -1, src)]
        
        for (i, j, d) in flights: graph[i][j] = d
            
        while Q:
            d, cross, start = heapq.heappop(Q)
            
            if cross in dists[start] or cross > k: continue
            if start == dst: return d
        
            dists[start][cross] = d
        
            for end in graph[start]:
                    heapq.heappush(Q, (d + graph[start][end],
                                       cross+1, end))
 
        return -1
