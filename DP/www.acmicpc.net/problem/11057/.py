N, LAST = int(input()), 10
DB = [[1]*LAST for _ in range(N)]

for n in range(1, N):
    for last in range(1, LAST):
        DB[n][last] = (DB[n][last-1]+DB[n-1][last])

print(sum(DB[-1]) % 10007)

