# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = []
        
        def dfs(root):
            if root.left: dfs(root.left)
            nodes.append(root.val)
            if root.right: dfs(root.right)
        
        dfs(root)
        
        return min(y-x for x, y in zip(
            nodes[:-1], nodes[1:]))
            