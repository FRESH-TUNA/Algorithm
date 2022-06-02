N, K = map(int, input().split())
Stuffs = [map(int, input().split()) for _ in range(N)]
DB = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    stuff_w, stuff_v = Stuffs[i-1]
    for w in range(K+1):
        if stuff_w > w:
            DB[i][w] = DB[i-1][w]
        else:
            DB[i][w] = max(
                DB[i-1][w], 
                DB[i-1][w-stuff_w] + stuff_v,
                DB[i][w-stuff_w] + stuff_v
            )
print(DB[-1][-1])
