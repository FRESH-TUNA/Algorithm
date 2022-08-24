import sys

input = sys.stdin.readline
N, DIVIDER = int(input()), 15746
DB = [0]*(N+1)

DB[0], DB[1] = 1, 1

for n in range(2, N+1):
    DB[n] = (DB[n-1]+DB[n-2]) % DIVIDER 

print(DB[N])

