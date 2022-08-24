import sys

input = sys.stdin.readline
N = int(input())
PACKS = [0]+list(map(int, input().split()))
DB = [[0]*(N+1) for _ in range(N+1)]

for m in range(1, N+1):
    for n in range(1, N+1):
        if n < m:
            DB[n][m] = DB[n][m-1]
        else:
            DB[n][m] = max(DB[n][m-1], DB[n-m][m-1]+PACKS[m], DB[n-m][m]+PACKS[m])
print(DB[-1][-1])

