def solution():
    N, M, K = map(int, input().split())
    DI, DJ = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]
    ND = ((1,3,5,7), (0,2,4,6))
    fires = []
    g = [[[] for _ in range(N)] for _ in range(N)]

    def fires_init():
        for _ in range(M):
            r, c, m, s, d = list(map(int, input().split()))
            fires.append([r-1, c-1, m, s, d])

    def move():
        while fires:
            r, c, m, s, d = fires.pop()
            nr = (r + s * DI[d]) % N
            nc = (c + s * DJ[d]) % N
            g[nr][nc].append([m, s, d])

    def all_odd_even(datas):
        res = datas[0][-1]&1
        for _, _, d in datas:
            if res != d&1: return 0
        return 1
    
    def merge():
        for r in range(N):
            for c in range(N):
                if len(g[r][c]) > 1:
                    nd = ND[all_odd_even(g[r][c])]
                    nm = sum(x[0] for x in g[r][c]) // 5
                    ns = sum(x[1] for x in g[r][c]) // len(g[r][c])

                    g[r][c].clear()
                    if not nm: continue
                    for d in nd:
                        fires.append([r, c, nm, ns, d])
                if len(g[r][c]) == 1:
                    fires.append([r, c] + g[r][c].pop())
    
    def call():
        fires_init()
        for _ in range(K):
            move()
            merge()
        print(sum([f[2] for f in fires]))
    call()

solution()
