class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums = [-10001] + nums
        result = [[-10001, -10001]] + [
            [0, 0] for _ in range(len(nums)-1)]
        # 0은 누적값, 1은 작은답
        for i in range(1, len(nums)):
            last_acc, last_ans = result[i-1]
            acc = last_acc + nums[i]        
            result[i][1] = max(nums[i], last_acc, acc, last_ans)
            result[i][0] = nums[i] if nums[i] > acc else acc

        return result[-1][1]
