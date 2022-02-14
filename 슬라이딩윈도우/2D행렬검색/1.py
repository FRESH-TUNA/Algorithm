# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        row, col = 0, len(matrix[0])-1
        
        while row <= len(matrix)-1 and col >= 0:
            if target == matrix[row][col]: return True
            elif target < matrix[row][col]: col -= 1
            elif target > matrix[row][col]: row += 1

        return False
        