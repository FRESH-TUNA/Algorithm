a = [0, 0, 1, 1, 2, 2]
target = 2
left, right = 0, len(a)-1

while left <= right:
    mid = left + (right - left) // 2
    if a[mid] <= target:
        left = mid+1
    else:
        right = mid-1
print(left)

left, right = 0, len(a)-1
while left <= right:
    mid = left + (right - left) // 2
    if a[mid] >= target:
        right = mid-1
    else:
        left = mid+1
print(left)
