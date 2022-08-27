import sys, heapq

input = sys.stdin.readline
N, MAX_ANSWER, BLOCK = int(input()), 2500, '0'
D, DR, DC = 4, (-1,0,1,0), (0,1,0,-1)
G = [list(input().rstrip()) for _ in range(N)]
DB = [[MAX_ANSWER]*N for _ in range(N)]
q = []

DB[0][0] = 0
heapq.heappush(q, (0,0,0))

while q:
    dist, r, c = heapq.heappop(q)
    for d in range(D):
        nr, nc = r+DR[d], c+DC[d]

        if nr==-1 or nr==N or nc==-1 or nc==N or DB[nr][nc]!=MAX_ANSWER:
            continue

        new_dist = dist + (G[nr][nc] == BLOCK)

        DB[nr][nc] = new_dist
        heapq.heappush(q, (new_dist,nr,nc))

print(DB[-1][-1])

