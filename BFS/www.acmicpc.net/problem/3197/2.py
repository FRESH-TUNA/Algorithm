from sys import stdin
from collections import deque

input = stdin.readline
R, C = map(int, input().split())
DR, DC, D, MAX_TIME = (-1,0,1,0), (0,1,0,-1), 4, R*C
tracing, water, lake, swan = deque(), deque(), [], []
next_tracing, next_water = deque(), deque()

traced = [[0]*C for _ in range(R)]
def init():
    for r in range(R):
        row = list(input().rstrip())
        for c in range(C):
            if row[c] == 'L':
                swan.append((r, c))
            if row[c] != 'X':
                water.append((r, c))
        lake.append(row)


def call():
    tracing.append(swan[0])
    
    for answer in range(MAX_TIME):
        if can_connect():
            return answer
        melting()

def melting():
    global water, next_water
    while water:
        r, c = water.popleft()

        for d in range(D):
            nr, nc = r+DR[d], c+DC[d]

            if nr==-1 or nr==R or nc==-1 or nc==C:
                continue
            if lake[nr][nc] == 'X':
                lake[nr][nc] = '.'
                next_water.append((nr, nc))
    water, next_water = next_water, water

    
def can_connect():
    global tracing, next_tracing, next_water
    while tracing:
        r, c = tracing.popleft()

        for d in range(D):
            nr, nc = r+DR[d], c+DC[d]

            if (nr, nc) == swan[1]:
                return True

            if nr==-1 or nr==R or nc==-1 or nc==C or traced[nr][nc]:
                continue

            traced[nr][nc] = 1
            if lake[nr][nc] == 'X':
                next_tracing.append((nr, nc))
            if lake[nr][nc] == '.':
                tracing.append((nr, nc))
    tracing, next_tracing = next_tracing, tracing
    return False

init()
print(call())

