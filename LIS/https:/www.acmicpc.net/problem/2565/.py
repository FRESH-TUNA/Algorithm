N = int(input())
Lines = sorted(list(map(int, input().split())) for _ in range(N))
DB = [0]*N

for n in range(N):
    for i in range(n):
        if Lines[n][1] > Lines[i][1]:
            DB[n] = max(DB[n], DB[i])
    DB[n] += 1

print(N - max(DB))
            
