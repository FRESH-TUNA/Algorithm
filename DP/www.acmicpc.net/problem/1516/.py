import sys

input = sys.stdin.readline
N = int(input())
DB, T, P = [0]*(N+1), [0]*(N+1), [[] for _ in range(N+1)]

def call():
    init()
    calculates()
    print('\n'.join(str(t) for t in DB[1:]))

def init():
    for n in range(1, N+1):
        datas = list(map(int, input().split()))
        T[n] = datas[0]

        for data in datas[1:]:
            if data == -1: break
            P[n].append(data)

def calculates():
    for n in range(1, N+1):
        if not DB[n]:
            calculate(n)

def calculate(n):
    p_time = 0
    for nn in P[n]:
        p_time = max(p_time, DB[nn] if DB[nn] else calculate(nn))
    DB[n] = T[n]+p_time
    return DB[n]

call()

