import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    M, DR, DC, D = 2**N, [-1,0,1,0], [0,1,0,-1], 4
    OVERFLOW = {-1, M} 
    G = [[list(map(int, input().split())) for _ in range(M)]]
    NG = [[[0 for _ in range(M)] for _ in range(M)]]
    GET, TRACED = 0, -1

    def firestorms():
        for L in map(int, input().split()):
            firestorm(L)
    
    def firestorm(L):
        rotate(0, 0, M, 2**L)
        swap()
        melting()
        swap()

    def rotate(row, col, width, L):
        if width == L:
            for r in range(L):
                for c in range(L):
                    NG[GET][row+c][col+L-1-r] = G[GET][row+r][col+c]
        else:
            new_width = width // 2
            for r in range(row, row+width, new_width):
                for c in range(col, col+width, new_width):
                    rotate(r, c, new_width, L)

    def swap():
        G[GET], NG[GET] = NG[GET], G[GET]
        
    def melting():
        for r in range(M):
            for c in range(M):
                if G[GET][r][c] and not cool(r, c):
                    NG[GET][r][c] = G[GET][r][c] - 1
                else:
                    NG[GET][r][c] = G[GET][r][c]

    def cool(r, c):
        ices = 0
        for d in range(D):
            nr, nc = r+DR[d], c+DC[d]
            if nr in OVERFLOW or nc in OVERFLOW:
                continue
            if G[GET][nr][nc]: ices += 1
        return ices >= 3
    
    def answer():
        total_ices, biggest_block = 0, 0
        for r in range(M):
            for c in range(M):
                if G[GET][r][c] and NG[GET][r][c] != TRACED:
                    blocks, ices = calc_ices(r, c)
                    total_ices += ices
                    biggest_block = max(biggest_block, blocks)
        print(total_ices)
        print(biggest_block)

    def calc_ices(r, c):
        q, blocks, ices = deque(), 0, 0

        q.append((r, c))
        NG[GET][r][c] = TRACED

        while q:
            r, c = q.popleft()
            blocks += 1
            ices += G[GET][r][c]
            for d in range(D):
                nr, nc = r+DR[d], c+DC[d]
                if nr in OVERFLOW or nc in OVERFLOW:
                    continue
                if G[GET][nr][nc] and NG[GET][nr][nc] != TRACED:
                    NG[GET][nr][nc] = TRACED
                    q.append((nr, nc))
        return blocks, ices
        
    firestorms()
    answer()

solution()

