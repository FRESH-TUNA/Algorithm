N, W = map(int, input().split())
DB = [[0] * (W+1) for _ in range(N+1)]
DATA = [[]] + [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    dw, dv = DATA[i]
    for w in range(W+1):
        if w < dw:
            DB[i][w] = DB[i-1][w]
        else:
            DB[i][w] = max(DB[i-1][w-dw] + dv, DB[i-1][w])
print(max(DB[-1]))
