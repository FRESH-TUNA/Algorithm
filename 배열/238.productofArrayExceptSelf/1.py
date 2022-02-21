class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_multiply, zero_counts, zero_idx = 1, 0, 0
        zero_include_answer = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0: 
                zero_counts += 1
                zero_idx = i
            else: all_multiply *= num
                
        if zero_counts >= 2: return zero_include_answer
        if zero_counts == 1:
            zero_include_answer[zero_idx] = all_multiply
            return zero_include_answer
        return [all_multiply // num for num in nums]