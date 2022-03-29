import sys

# global
input = sys.stdin.readline
N, DB = 0, []

def calc():
    DB[1], DB[2] = 1, 3
    for i in range(3, N+1): 
        DB[i] = (DB[i-2]*2 + DB[i-1]) % 10007

# driver
N = int(input())
DB = [0] * (N+1)
calc()
print(DB[N])
