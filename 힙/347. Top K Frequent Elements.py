class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        db = collections.Counter(nums)
        Q = []
        answer = []
        
        for num in db: 
            heapq.heappush(Q, (db[num] * (-1), num))
        
        while k:
            k -= 1
            answer.append(heapq.heappop(Q)[1])
            
        return answer
        