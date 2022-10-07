import heapq

def solution(n, works):
    works = [w*(-1) for w in works]
    heapq.heapify(works)

    while n:
        work = heapq.heappop(works)
        if work == 0:
            return 0
        else:
            heapq.heappush(works, work+1)
        n -= 1
        
    return sum(work**2 for work in works)

