from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
G = [list(stdin.readline().rstrip()) for _ in range(N)]
DB = [[-1]*M for _ in range(N)]
D, DR, DC, BLOCK = 4, (-1,0,1,0), (0,1,0,-1), '1'
rq, cq = deque(), deque()

rq.append(0)
cq.append(0)
DB[0][0] = 0

while rq:
    r, c = rq.popleft(), cq.popleft()

    for d in range(D):
        nr, nc = r+DR[d], c+DC[d]
        if nr==-1 or nr==N or nc==-1 or nc==M or DB[nr][nc]!=-1:
            continue
        if G[nr][nc] == BLOCK:
            DB[nr][nc] = DB[r][c]+1
            rq.append(nr)
            cq.append(nc)
        else:
            DB[nr][nc] = DB[r][c]
            rq.appendleft(nr)
            cq.appendleft(nc)

print(DB[-1][-1])

