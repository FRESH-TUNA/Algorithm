N = int(input())
NUMS = list(map(int, input().split()))
DBA, DBD = [1] * N, [1] * N

for i in range(N):
    for j in range(i):
        if NUMS[i] > NUMS[j]:
            DBA[i] = max(DBA[i], DBA[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if NUMS[i] > NUMS[j]:
            DBD[i] = max(DBD[i], DBD[j]+1)

print(max(x+y-1for (x, y) in zip(DBA, DBD)))