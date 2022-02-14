class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        answer = []
        
        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()

            while q:
                if nums[q[-1]] < nums[i]: q.pop()
                else: break
            
            q.append(i)
            if i >= k - 1: answer.append(nums[q[0]])
        
        return answer
                
            