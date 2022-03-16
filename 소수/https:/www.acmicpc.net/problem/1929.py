import sys

M, N = 0, 0
DB = []

def solution():
    for base in range(2, N+1):
        if not DB[base]: continue
        for i in range(base*2, N+1, base): DB[i] = 0
    return filter(lambda x: DB[x], range(M, N+1))

# driver
input = sys.stdin.readline
M, N = map(int, input().split())
DB, DB[1] = [1] * (N+1), 0
print('\n'.join(map(str, solution())))
