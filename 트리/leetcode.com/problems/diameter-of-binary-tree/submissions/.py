class Solution:
    answer = 0
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        left = self.dfs(root.left) if root.left != None else 0
        right = self.dfs(root.right) if root.right != None else 0
        
        self.answer = max(self.answer, left+right)
        return max(left+1, right+1)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer
