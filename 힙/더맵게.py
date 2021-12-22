import heapq

def solution(scoville, K):
    # 힙에 최적화된 구조
    heapq.heapify(scoville)
    count = 0
    
    # loop
    while True:
        if scoville[0] >= K: return count
        elif len(scoville) == 1: return -1
        else:
            a, b = heapq.heappop(scoville), heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            count += 1
    