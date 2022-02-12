import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        datas, answer = [], []
        for (x, y) in points:
            heapq.heappush(datas, (x ** 2 + y ** 2, x, y))
        while k:
            k -= 1
            answer.append(heapq.heappop(datas)[1:])
        return answer
        
        