class Solution:
    def combine(self, n: int, MAX_DEPTH: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            if not k: 
                results.append(elements[:])
                return
            for i in range(start, n+1)
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        return results
