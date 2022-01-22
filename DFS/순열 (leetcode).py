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