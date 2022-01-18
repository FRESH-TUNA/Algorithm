class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0: answer, 1: last_index
        db = [(0, -1)] + [None for i in range(len(nums))]
        nums = [0] + nums
        
        for i in range(1, len(nums)):
            if db[i-1][1] + 1 == i:
                db[i] = max(db[i-1], (db[i-2][0] + nums[i], i))
            else:
                db[i] = (db[i-1][0] + nums[i], i)
        
        return db[-1][0]
        