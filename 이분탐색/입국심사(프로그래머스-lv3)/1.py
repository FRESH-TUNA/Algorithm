def solution(n, times):
    left, right = 0, max(times) * n
    while left < right:
        result, mid = 0, (left + right) // 2
        for t in times: result += mid // t
        if result >= n: right = mid
        else: left = mid + 1
    return left
