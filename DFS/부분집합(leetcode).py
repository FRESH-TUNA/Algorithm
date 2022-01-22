class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, END = [[]], len(nums)
        self.dfs(ans, nums, [], 0, END)
        return ans
        
    def dfs(self, ans, nums, cur, start, END):
        if start == END: return    
        
        for i in range(start, END):
            cur.append(nums[i])
            ans.append(cur[:])
            self.dfs(ans, nums, cur, i+1, END)
            cur.pop()
