import bisect

N = int(input())
nums = list(map(int, input().rsplit()))
DB = [nums[0]]

for num in nums:
    if num > DB[-1]: DB.append(num)
    else:
        j = bisect.bisect_left(DB, num)
        DB[j] = num
print(len(DB))
