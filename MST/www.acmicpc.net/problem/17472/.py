from collections import deque

def solution():
    N, M = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    D, DI, DJ = 4, [-1,0,1,0], [0,1,0,-1]
    candidates = []
    LANDS, GET = [2], 0

    def get_candidate(i, j, d):
        start, dist = G[i][j], 0

        while True:
            i, j = i+DI[d], j+DJ[d]
            if i==-1 or i==N or j==-1 or j==M:
                break
            if G[i][j] != 0:
                if dist >= 2:
                    candidates.append((dist, start, G[i][j]))
                return
            dist += 1

    def get_candidates():
        for i in range(N):
            for j in range(M):
                if G[i][j]:
                    for d in range(D):
                        get_candidate(i, j, d)
        candidates.sort()

    def set_lands():
        for i in range(N):
            for j in range(M):
                if G[i][j] == 1:
                    bfs(i, j)
    def bfs(i, j):
        Q = deque()
        Q.append((i, j))
        land = LANDS[GET]
        G[i][j] = land
        
        while Q:
            i, j = Q.popleft()
            for d in range(D):
                ni, nj = i+DI[d], j+DJ[d]
                if ni==-1 or ni==N or nj==-1 or nj == M:
                    continue
                if G[ni][nj] != 1:
                    continue
                G[ni][nj] = land
                Q.append((ni, nj))
        LANDS[GET] += 1

    def union(parents, start, end):
        start, end = parent(parents, start), parent(parents, end)
        parents[start] = parents[end] = min(start, end)

    def parent(parents, node):
        if parents[node] == node:
            return node
        parents[node] = parent(parents, parents[node])
        return parents[node]

    def determine(parents):
        root = parent(parents, 2)
        for n in range(3, LANDS[GET]):
            if root != parent(parents, n):
                return False
        return True
        
    def calculate():
        parents = [i for i in range(LANDS[GET])]
        result = 0
    
        for dist,start,end in candidates:
            if parent(parents, start) != parent(parents, end):
                result += dist
                union(parents, start, end)
        print([-1, result][determine(parents)])

    # driver
    set_lands()
    get_candidates()
    calculate()
     
solution()
