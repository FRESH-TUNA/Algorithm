from collections import deque

def solution():
    N, M, K = list(map(int, input().split()))
    g = [list(map(int, input().split())) for _ in range(N)]
    D, DN = [0]+list(map(int, input().split())), 4
    DI, DJ = [0,-1,1,0,0], [0,0,0,-1,1]
    P = [None] + [[None]+[list(map(int, input().split())) 
                for _ in range(DN)] for _ in range(M)]
    T, GET, OUT_OF_BOUND = 1000, 0, {-1,N}

    st, sr = [[0]*N for _ in range(N)], [[0]*N for _ in range(N)]
    fishes, removed = deque(), [0]

    def move_fishes():
        for _ in range(len(fishes)):
            move_fish(*fishes.popleft())

    def move_fish(fish, i, j):
        d = D[fish]
        pd, pi, pj = None, None, None

        # 방향에 따라 우선순위 대로 검사
        for nd in P[fish][d]:
            ni, nj = i+DI[nd], j+DJ[nd]
            if ni in OUT_OF_BOUND or nj in OUT_OF_BOUND:
                continue
            if st[ni][nj] == fish:
                pi, pj, pd = ni, nj, nd
            if st[ni][nj]:
                continue
            fishes.append((fish, ni, nj))
            D[fish] = nd
            return
        fishes.append((fish, pi, pj))
        D[fish] = pd

    def kill_fishes():
        while fishes:
            fish, i, j = fishes.popleft()
            if g[i][j] == 0: 
                g[i][j] = fish
            else:
                removed[GET] += 1
                g[i][j] = min(g[i][j], fish)

    def init():
        for i in range(N):
            for j in range(N):
                if g[i][j]:
                    fishes.append((g[i][j], i, j))
                    st[i][j], sr[i][j], g[i][j] = g[i][j], K, 0
                elif sr[i][j] > 1:
                    sr[i][j] -= 1
                else:
                    st[i][j], sr[i][j] = 0, 0

    def simulate():
        for t in range(1, T+1):
            move_fishes()
            kill_fishes()
            # for row in sr:
            #     print(row)
            # print(str(t)+"--")
            init()
            if removed[GET] == M-1: return t
        return -1

    for row in P:
        print(row)
    init()
    print(simulate())
    
solution()
