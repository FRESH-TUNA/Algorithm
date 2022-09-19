def solution(que1, que2):
    queSum = (sum(que1) + sum(que2))
    if queSum & 1:
        return -1
    
    target = queSum // 2

    n, cur = len(que1), sum(que1)
    start, end, answer = 0, n - 1, 0
    que3 = que1 + que2
    
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans

