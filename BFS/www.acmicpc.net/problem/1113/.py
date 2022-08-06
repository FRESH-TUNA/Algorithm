from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
DR, DC, D, GET, MAX_HEIGHT = [-1, 0, 0, 1], [0, -1, 1, 0], 4, 0, 9
answer = [0]

def bfs(r, c, n, visited):
    Q = deque([(r, c)])
    can_pool = True
    water = visited[r][c] = 1

    while Q:
        r, c = Q.popleft()
        for d in range(D):
            nr, nc = r+DR[d], c+DC[d]
            if nr==-1 or nr==N or nc==-1 or nc==M:
                can_pool = False
                continue
            if board[nr][nc]<n and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                water += 1
    return water if can_pool else 0

def solution():
    answer = 0
    
    for num in range(1, MAX_HEIGHT+1):
        visited = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] < num and not visited[i][j]:
                    answer += bfs(i, j, num, visited)
    print(answer)

solution()

