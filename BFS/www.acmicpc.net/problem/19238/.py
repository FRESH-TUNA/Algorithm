import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M, FUEL = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    S = [[-1]*N for _ in range(N)]
    I, J = map(int, input().split())
    PASSENGERS = [list(map(int, input().split())) for _ in range(M)]
    DI, DJ, DN = [-1,0,0,1], [0,-1,1,0], 4

    FUEL, CHECKED, GET = [FUEL], [0], 0

    def start_point_init():
        for idx, value in enumerate(PASSENGERS):
            i, j, _, _ = value
            S[i-1][j-1] = idx

    def optimized_passenger(target):
        return sorted(target, key=lambda k: PASSENGERS[k])[0]
        
    def find_passenger(i, j):
        Q = deque()
        target = []

        if S[i][j] != -1:
            return S[i][j], 0
        
        traced, dist = [[0]*N for _ in range(N)], 1
        Q.append((i,j))
        traced[i][j] = 1

        while Q:
            for _ in range(len(Q)):
                i, j = Q.popleft()
                for d in range(DN):
                    ni, nj = i+DI[d], j+DJ[d]
                    if ni==-1 or ni==N or nj==-1 or nj==N:
                        continue
                    if traced[ni][nj] or G[ni][nj]:
                        continue
                    if S[ni][nj] != -1:
                        target.append(S[ni][nj])
                    traced[ni][nj] = 1
                    Q.append((ni, nj))

            if target: return optimized_passenger(target), dist
            dist += 1
        return -1, -1

    def distance(i, j, ti, tj):
        Q = deque()
        traced, dist = [[0]*N for _ in range(N)], 1

        Q.append((i,j))
        traced[i][j] = 1

        while Q:
            for _ in range(len(Q)):
                i, j = Q.popleft()
                for d in range(DN):
                    ni, nj = i+DI[d], j+DJ[d]
                    if ni==-1 or ni==N or nj==-1 or nj==N:
                        continue
                    if traced[ni][nj] or G[ni][nj]:
                        continue
                    if ni==ti and nj==tj:
                        return dist
                    traced[ni][nj] = 1
                    Q.append((ni, nj))
            dist += 1
        return -1
    
    def service(i, j):
        while CHECKED[GET] < M:
            p, dist = find_passenger(i, j)

            if p==-1 or FUEL[GET] < dist:
                return -1
            FUEL[GET] -= dist
            
            i, j, ni, nj = PASSENGERS[p]
            S[i-1][j-1] = -1
            dist = distance(i-1, j-1, ni-1, nj-1)
            if dist==-1 or FUEL[GET] < dist:
                return -1
            
            i, j = ni-1, nj-1
            FUEL[GET] += dist
            CHECKED[GET] += 1
        return FUEL[GET] 
    
    start_point_init()
    print(service(I-1, J-1))

solution()
