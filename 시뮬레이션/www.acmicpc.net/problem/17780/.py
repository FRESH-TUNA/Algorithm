from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INFO = [list(map(int, input().split())) for _ in range(N)]
G = [[deque() for _ in range(N)] for _ in range(N)]
DR, DC, DN, MAX_GAME, OUT = (0,0,-1,1), (1,-1,0,0), 4, 1000, {-1,N}
REVERSE, R, C, D = {0:1, 1:0, 2:3, 3:2}, 0, 1, 2
WHITE, RED, BLUE = 0, 1, 2
blocks, q = [], deque()

def graph():
    for k in range(K):
        a, b, d = map(int, input().split())
        G[a-1][b-1].append(k)
        blocks.append([a-1, b-1, d-1])
        
def gaming():
    for g in range(1, MAX_GAME+1):
        for k in range(K):
            if move(k): return g
    return -1

def move(k):
    r, c, d = blocks[k]
    nr, nc = r+DR[d], c+DC[d]

    # can move
    if G[r][c][0] != k:
        return False
    
    # blue move
    if nr in OUT or nc in OUT or INFO[nr][nc] == BLUE:
        blocks[k][D] = d = REVERSE[d]
        nr, nc = r+DR[d], c+DC[d]
        if nr in OUT or nc in OUT or INFO[nr][nc] == BLUE:
            return False

    while not q or q[-1] != k:
        q.append(G[r][c].pop())

    if INFO[nr][nc] == WHITE:
        while q:
            block = q.pop()
            G[nr][nc].append(block)
            blocks[block][R], blocks[block][C] = nr, nc
    else: 
        while q:
            block = q.popleft()
            G[nr][nc].append(block)
            blocks[block][R], blocks[block][C] = nr, nc

    return len(G[nr][nc]) >= 4
    
graph()
print(gaming())

