import sys

input = sys.stdin.readline
N, M = map(int, input().split())
DB = [0] + list(map(int, input().split()[:N]))

for i in range(1, N+1): DB[i] += DB[i-1]
for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    print(DB[end]-DB[start])
