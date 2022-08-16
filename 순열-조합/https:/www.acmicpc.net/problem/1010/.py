from collections import deque
import sys

input = sys.stdin.readline
MAX_NM = 30
DB = [[0]*(MAX_NM+1) for _ in range(MAX_NM+1)]
N = int(input())

def init():
    DB[0][0] = DB[1][0] = DB[1][1] = 1

    for i in range(MAX_NM+1):
        DB[i][0] = DB[i][i] = 1

    for i in range(2, MAX_NM+1):
        for j in range(1, i):
            DB[i][j] = DB[i-1][j-1] + DB[i-1][j]

def call():
    for _ in range(N):
        a, b = map(int, input().split())
        print(DB[b][a])
    
init()
call()

