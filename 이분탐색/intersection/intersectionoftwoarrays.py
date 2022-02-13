class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        answer = set()
        for num in nums1:
            if self.search(nums2, num):
                answer.add(num)         
        return list(answer)

    def search(self, nums, num):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > num: right = mid - 1
            elif nums[mid] < num: left = mid + 1
            else: return True
        return False