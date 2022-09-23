import heapq

def solution(n, paths, gates, summits):
    answer, q = [], []
    MAX_INTENSITY = 10000000
    G = [[] for _ in range(n+1)]
    intensities = [MAX_INTENSITY]*(n+1)
    summits, gates = set(summits), set(gates)
    
    def init():
        for i,j,t in paths:
            G[i].append((j,t))
            G[j].append((i,t))
        for gate in gates:
            heapq.heappush(q, (0,gate))
            intensities[gate] = 0
    
    def call():
        while q:
            intensity, node = heapq.heappop(q)
            
            if intensities[node] < intensity:
                continue

            for next_node, time in G[node]:
                if next_node in gates:
                    continue
                
                new_intensity = max(intensity, time)

                if intensities[next_node] > new_intensity:
                    intensities[next_node] = new_intensity
                    if next_node not in summits:
                        heapq.heappush(q, (new_intensity, next_node))
        return min([intensities[summit], summit] for summit in summits)[::-1]

    init()
    return call()

