import sys

# global
input = sys.stdin.readline
N, DB = 0, []

def solution():
    DB[1] = 1
    for n in range(2, N+1):
        ans = 50000
        for i in range(1, N+1):
            if n - i*i < 0: break
            ans = min(ans, 1+DB[n-i*i])
        DB[n] = ans
    print(DB[N])

# driver
N = int(input())
DB = [0] * (N+1)
solution()
