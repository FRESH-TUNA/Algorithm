from collections import deque
import sys

# global
input = sys.stdin.readline
N, DB, RES = 0, [], []

def calc(): 
    for i in range(N): bfs(i)

def bfs(i):
    Q = deque()
    Q.append(i)

    while Q:
        ni = Q.pop()
        for nj in range(N):
            if DB[ni][nj] and not RES[i][nj]:
                RES[i][nj] = 1
                Q.appendleft(nj)

def result():
    for i in range(N): 
        print(" ".join(str(c) for c in RES[i]))
    
# driver
N = int(input())
DB = [list(map(int, input().split()[:N])) for _ in range(N)]
RES = [[0] * N for _ in range(N)]
calc()
result()
