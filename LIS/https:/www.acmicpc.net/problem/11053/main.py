N = int(input())
NUMS = list(map(int, input().split()))
DB = [1] * N

for i in range(N):
    for j in range(i):
        if NUMS[i] > NUMS[j]:
            DB[i] = max(DB[i], DB[j]+1)

print(max(DB))
