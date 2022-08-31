import sys, heapq

input = sys.stdin.readline
N = int(input())
G = [list(input().rstrip()) for _ in range(N)]
D, DR, DC, MAX_ANSWER = 4, (-1,0,1,0), (0,1,0,-1), N*N+N
DB = [[[MAX_ANSWER]*D for _ in range(N)] for _ in range(N)]

doors, DOOR, DOOR_MAX, GLASS, WALL = [], "#", 2, "!", "*"

def findDoors():
    for i in range(N):
        for j in range(N):
            if G[i][j] == DOOR:
                for d in range(D):
                    nr, nc = i+DR[d], j+DC[d]
                    if nr!=-1 and nr!=N and nc!=-1 and nc!=N and G[nr][nc]!=WALL:
                        doors.append((0,i,j,d))
                        break
            if len(doors) == DOOR_MAX: return

def answer():
    sans, sr, sc, sd = doors[0]
    dans, dr, dc, dd = doors[1]
    DB[sr][sc] = [0,0,0,0]
    q = []
    q.append((0, sr, sc, sd))
    
    while q:
        ans, r, c, d = heapq.heappop(q)
        if r==dr and c==dc:
            break
        
        if DB[r][c][d] < ans:
            continue

        nr, nc = r+DR[d], c+DC[d]
        if nr!=-1 and nr!=N and nc!=-1 and nc!=N and ans<DB[nr][nc][d] and G[nr][nc]!=WALL:
            DB[nr][nc][d] = ans
            heapq.heappush(q, (ans, nr, nc, d))

        if G[r][c] != GLASS:
            continue

        for nd in range(D):
            nr, nc = r+DR[nd], c+DC[nd]
            if nr==-1 or nr==N or nc==-1 or nc==N or G[nr][nc]==WALL:
                continue
            # if DB[nr][nc][nd] != MAX_ANSWER and ans >= DB[nr][nc][nd]:
            #     DB[nr][nc][nd] = ans
            #     heapq.heappush(q, (ans, nr, nc, nd))
            #     continue
            if (ans+1) >= DB[nr][nc][nd]:
                continue
            DB[nr][nc][nd] = ans+1
            heapq.heappush(q, (ans+1, nr, nc, nd))
    print(min(DB[dr][dc]))
 
findDoors()
answer()

