import sys

# global
input = sys.stdin.readline
N, DB = 0, []

def calc():
    for n in range(N):
        for s in range(N):
            for e in range(N):
                if DB[s][n] and DB[n][e]: DB[s][e] = 1

def result():
    for i in range(N): 
        print(" ".join(str(c) for c in DB[i]))

# driver
N = int(input())
DB = [list(map(int, input().split()[:N])) for _ in range(N)]
calc()
result()
