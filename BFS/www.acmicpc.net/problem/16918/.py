from collections import deque
import sys

input = sys.stdin.readline
R, C, N = map(int, input().split())
DR, DC, D, TIMER = (-1,0,1,0), (0,1,0,-1), 4, 1
graph = [[0]*C for _ in range(R)]

def init_graph():
    for r in range(R):
        line = list(input().rstrip())
        for c in range(C):
            graph[r][c] = -1 if line[c] == '.' else TIMER

def call():
    for n in range(N-1):
        if n & 1 == 0:
            set_bomb()
        else:
            pungs()
    result()

def set_bomb():
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                graph[r][c] -= 1
            else:
                graph[r][c] = TIMER

def pungs():
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 0:
                pung(r, c)
                

def pung(r, c):
    q = deque()
    q.append((r, c))
    graph[r][c] = -1
    
    while q:
        r, c = q.popleft()
        for d in range(D):
            nr, nc = r+DR[d], c+DC[d]
            if nr==-1 or nr==R or nc==-1 or nc==C or graph[nr][nc]==-1:
                continue
            if graph[nr][nc] == 0:
                q.append((nr, nc))
            graph[nr][nc] = -1

def result():
    for row in graph:
        print(''.join('.' if x==-1 else 'O' for x in row))

    
init_graph()
call()

