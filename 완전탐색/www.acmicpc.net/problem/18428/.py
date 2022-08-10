from collections import deque
from itertools import product, combinations
import sys

input = sys.stdin.readline
N = int(input())
BLANK, STUDENT, TEACHER, BLOCK = 'X', 'S', 'T', 'O'
DR, DC, D = (-1,0,1,0), (0,1,0,-1), 4
TEACHERS = []
G, CHECKED = [input().rstrip().split() for _ in range(N)], 1

def call():
    for case in make_cases():
        if check(case):
            print("YES")
            return
    
    print("NO")

def make_cases():
    blanks = []
    for i in range(N):
        for j in range(N):
            if G[i][j] == BLANK:
                blanks.append((i, j))
            if G[i][j] == TEACHER:
                TEACHERS.append((i, j))
    return combinations(blanks, 3)

def check(case):
    def bfs(r, c):
        for d in range(D):
            nr, nc = r, c
            while True:
                nr, nc = nr+DR[d], nc+DC[d]
                if nr==-1 or nr==N or nc==-1 or nc==N or G[nr][nc]==BLOCK:
                    break
                if G[nr][nc] == STUDENT:
                    return False
        return True

    for i, j in case:
        G[i][j] = BLOCK

    for i, j in TEACHERS:
        if not bfs(i, j):
            for i, j in case:
                G[i][j] = BLANK
            return False
                
    for i, j in case:
        G[i][j] = BLANK
    return True

call()

