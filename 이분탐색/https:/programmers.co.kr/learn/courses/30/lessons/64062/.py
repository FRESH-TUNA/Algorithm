def solution(stones, k):
    left, right = 1, 200_000_000
    
    while left <= right:
        mid = left + (right-left) // 2
        jump = 0
        
        for s in stones:
            if s > mid:
                jump = 0
            else: jump += 1
            if jump == k: break
        
        if jump != k:
            left = mid+1
        else:
            right = mid-1
    return left 
