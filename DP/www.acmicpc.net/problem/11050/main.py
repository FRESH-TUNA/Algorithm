import sys

# global
input = sys.stdin.readline
N, M = 0, 0

def solution():
    DB = [1] * (N+1)
    for i in range(1, N+1): DB[i] *= i*DB[i-1]
    print(DB[N] // DB[N-M] // DB[M])
    
# driver
N, M = map(int, input().split())
solution()
