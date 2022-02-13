class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[left] <= nums[right]: left = right + 1
            else: right = mid - 1
        pivot = left
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1
            