import bisect

N = int(input())
nums = list(map(int, input().split()))
DB, MAX = [1] * N, [nums[0]]

for i in range(1, N):
    if nums[i] > MAX[-1]:
        MAX.append(nums[i])
        DB[i] = len(MAX)
    else:
        j = bisect.bisect_left(MAX, nums[i])
        MAX[j] = nums[i]
        DB[i] += j

max_idx, max_db, res = DB.index(max(DB)), max(DB), []

while max_idx >= 0:
    if DB[max_idx] == max_db:
        res.append(nums[max_idx])
        max_db -= 1
    max_idx -= 1

print(len(MAX))
print(*reversed(res))
