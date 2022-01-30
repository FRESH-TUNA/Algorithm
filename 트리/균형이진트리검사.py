# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        def check(node):
            if not node: return 0
            
            left, right = 0, 0
            if node.left: left = check(node.left)
            if node.right: right = check(node.right)
            
            if abs(left - right) > 1: self.balanced = False
            
            return max(left, right) + 1
   
        check(root)
        return self.balanced
