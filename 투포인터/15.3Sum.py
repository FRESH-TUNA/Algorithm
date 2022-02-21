class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            if i > 0 and nums[i] == nums[i-1]: continue
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                        
                if result > 0: right -= 1
                elif result < 0: left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results