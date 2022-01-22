class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cases = []
        self.dfs(cases, candidates, [], 0, target // min(candidates) + 1)
        return list(filter(lambda x: sum(x) == target, cases))
    
    def dfs(self, cases, candidates, cur, start, border):
        if not border: return
        
        for i in range(start, len(candidates)):
            cur.append(candidates[i])
            cases.append(cur[:])
            self.dfs(cases, candidates, cur, i, border-1)
            cur.pop()