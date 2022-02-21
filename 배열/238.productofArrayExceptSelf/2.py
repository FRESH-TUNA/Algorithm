class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        answer = []
        for idx in range(len(nums)): 
            answer.append(acc)
            acc *= nums[idx]
            
        acc = 1
        for idx in range(len(nums)-1, -1, -1):
            answer[idx] *= acc
            acc *= nums[idx]

        return answer
            