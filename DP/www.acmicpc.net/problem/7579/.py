import sys

N, M = map(int, sys.stdin.readline().split())
MEMORY = [0] + list(map(int, sys.stdin.readline().split()))
COST = [0] + list(map(int, sys.stdin.readline().split()))
COST_N, MAX_COST = len(COST), sum(COST) + 1
DB = [[0 for _ in range(MAX_COST)] for __ in range(COST_N + 1)]
result = 100000000000

for i in range(1, COST_N):
    for j in range(MAX_COST):
        if COST[i] > j:
            DB[i][j] = DB[i-1][j]
        else:
            DB[i][j] = max(DB[i-1][j-COST[i]] + MEMORY[i], DB[i-1][j])

        if DB[i][j] >= M:
            result = min(result, j)

print([0,result][M!=0])

