import sys, heapq

def solution():
    input = sys.stdin.readline
    X1, Y1, X2, Y2 = map(int, input().split())
    N = int(input())
    paths = [[X1, Y1], [X2, Y2]
            ] + [list(map(int, input().split())) for _ in range(N)]
    M, MAX_DIST = len(paths), 10000
    dists, primes = [10000]*M, [1]*MAX_DIST
    G = [[] for _ in range(M)]
    START, END = 0, 1

    def prime():
        primes[0] = primes[1] = 0
        for n in range(2, int(MAX_DIST**0.5)):
            if primes[n] == 0: continue
            for value in range(n+n, MAX_DIST, n):
                primes[value] = 0

    def graph():
        for node in range(M):
            for new_node in range(M):
                dist = distance(node, new_node)
                if primes[dist]:
                    G[node].append((dist, new_node))
        
    def distance(start, end):
        si, sj = paths[start]
        ei, ej = paths[end]
        return int(((si-ei)**2 + (sj-ej)**2)**0.5)
        
    def dijkstra(): 
        Q = []
        
        Q.append((0, START))
        dists[START] = 0
        while Q:
            dist, node = heapq.heappop(Q)

            if dists[node] < dist: continue
            if node == END: break

            for new_dist, new_node in G[node]:
                if dists[new_node] > dists[node] + new_dist:
                    dists[new_node] = dists[node] + new_dist
                    heapq.heappush(Q, (dists[new_node], new_node))
        print([dists[END], -1][dists[END] == MAX_DIST])

    prime()
    graph()
    dijkstra()

solution()
