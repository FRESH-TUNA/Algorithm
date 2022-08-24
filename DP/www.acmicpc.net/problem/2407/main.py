import sys

MAX_N = 100
N, M, DB = 0, 0, None

def input():
    global N, M, DB, MAX_N
    i = sys.stdin.readline
    N, M = map(int, i().split())
    DB = [[['0']*MAX_N for _ in range(i+1)] for i in range(N+1)]
    DB[0][0][0], DB[1][0][0], DB[1][1][0] = '1', '1', '1'

def solution():
    global N, M, DB
    for i in range(2, N+1):
        DB[i][0][0] = '1'
        for j in range(1, i): calculate(i, j)
        DB[i][i][0] = '1'
    print(int(''.join(reversed(DB[N][M]))))

def calculate(i, j):
    global MAX_N
    carry = 0

    for idx in range(MAX_N):
        res = int(DB[i-1][j-1][idx]) + int(DB[i-1][j][idx]) + carry
        res, carry = res % 10, res // 10
        DB[i][j][idx] = str(res)

input()
solution()
