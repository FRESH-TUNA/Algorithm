from collections import deque

def solution():
    N, M, K = map(int, input().split())
    G = [[[[] for _ in range(N+1)] for _ in range(N+1)]]
    MG = [[[[] for _ in range(N+1)] for _ in range(N+1)]]
    NG = [[[[] for _ in range(N+1)] for _ in range(N+1)]]
    DI, DJ = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
    ND = ((1,3,5,7), (0,2,4,6))
    GET = 0
    
    def graph():
        for _ in range(M):
            i, j, m, s, d = map(int, input().split())
            G[GET][i][j].append((m,s,d))

    def move():
        for i in range(1, N+1):
            for j in range(1, N+1):
                while G[GET][i][j]:
                    m, s, d = G[GET][i][j].pop()
                    ni, nj = new_ij(i, j, s, d)
                    MG[GET][ni][nj].append((m,s,d))
        
    def merge():
        for i in range(1, N+1):
            for j in range(1, N+1):
                datas = MG[GET][i][j]
                
                if not datas: 
                    continue
                    
                if len(datas) == 1:
                    NG[GET][i][j], MG[GET][i][j] = MG[GET][i][j], NG[GET][i][j]
                    continue
                    
                nm = sum(x[0] for x in datas) // 5
                ns = sum(x[1] for x in datas) // len(datas)
                if not nm:
                    MG[GET][i][j].clear()
                    continue
                for d in ND[all_odd_even(datas)]:
                    NG[GET][i][j].append((nm,ns,d))
                MG[GET][i][j].clear()

        G[GET], NG[GET] = NG[GET], G[GET]

    def all_odd_even(datas):
        last = datas[0][2]&1
        for data in datas:
            if last != data[2]&1:
                return 0
        return 1

    def new_ij(i, j, s, d):
        for _ in range(s):
            i, j = i+DI[d], j+DJ[d]        
            if i == 0: i = N
            if i == N+1: i = 1
            if j == 0: j == N
            if j == N+1: j = 1
        return i, j

    def calculate():
        answer = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if len(G[GET][i][j]): 
                    answer += sum(x[0] for x in G[GET][i][j])
        return answer

    def call():
        graph()
        for _ in range(K):
            move()
            merge()
        return calculate()

    return call()
    
print(solution())
