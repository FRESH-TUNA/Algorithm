class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        traced = [[0 for _ in range(len(grid[i]))] 
                     for i in range(len(grid))]
        answer = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not traced[i][j] and grid[i][j] == "1": 
                    answer += self.dfs(grid, traced, i, j)
        return answer
    
    def dfs(self, grid, traced, i, j):
        stack, cases = [(i,j)], [(-1,0), (1,0), (0,-1), (0,1)]
        ROW, COL = len(grid), len(grid[0])
        while stack:
            i, j = stack.pop()
            traced[i][j] = 1
            
            for (_i, _j) in cases:
                n_i, n_j = i + _i, j + _j
                if not (n_i in range(0, ROW) 
                        and n_j in range(0, COL)
                        and grid[n_i][n_j] == "1"
                       ) or traced[n_i][n_j]: continue
                stack.append((n_i, n_j))
        return 1