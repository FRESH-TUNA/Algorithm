class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer, stack, MAX_DEPTH = [], [(set(), [])], len(nums)
        
        while stack:
            db, _ans = stack.pop()
            
            if len(_ans) == MAX_DEPTH:
                answer.append(_ans)
            else:
                for num in nums:
                    if num in db: continue
                    stack.append(({x for x in db} | {num}, _ans + [num]))
        return answer



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, ans, [])
        return ans
    
    def dfs(self, nums, ans, cur):
        if len(cur) == len(nums): ans.append(cur)
        else:
            for num in nums:
                if num not in cur: 
                    self.dfs(nums, ans, cur + [num])
            