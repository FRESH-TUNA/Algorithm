class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = collections.deque()
        answer = []
        
        for i, num in enumerate(nums):
            if Q and i - Q[0] >= k: Q.popleft()
            
            while Q:
                if nums[i] > nums[Q[-1]]: Q.pop()
                else: break
                
            Q.append(i)
            if i >= k-1: answer.append(nums[Q[0]])
        
        return answer

            