import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    ALPHA = 0
    LEFT = ((-2,0,0.02), (2,0,0.02),
            (-1,-1,0.1), (1,-1,0.1),
            (-1,1,0.01), (1,1,0.01),
            (-1,0,0.07), (1,0,0.07),
            (0,-2,0.05), (0,-1,ALPHA))
    DR, DC, DN = (0,1,0,-1), (-1,0,1,0), 4
    SP = (tuple((r,c,p) for r,c,p in LEFT),
          tuple((-c,r,p) for r,c,p in LEFT),
          tuple((r,-c,p) for r,c,p in LEFT),
          tuple((c,r,p) for r,c,p in LEFT))

    def distribute(r, c, d):
        outbound, distributed = 0, 0
        
        for dr, dc, p in SP[d]:
            cr, cc = r+dr, c+dc

            if p==ALPHA:
                moved = G[r][c]-distributed
            else:
                moved = int(G[r][c]*p)
                distributed += moved

            if 0<=cr<N and 0<=cc<N:
                G[cr][cc] += moved
            else:
                outbound += moved
        G[r][c] = 0
        return outbound

    def call():
        r, c, d, move = N//2, N//2, 0, 1
        outbound = 0
        
        while True:
            for _ in range(move):
                r, c = r+DR[d], c+DC[d]
                if c==-1: return outbound
                outbound += distribute(r, c, d)
            d = (d+1) % DN
            if d==0 or d==2: move += 1                
    print(call())

solution()
