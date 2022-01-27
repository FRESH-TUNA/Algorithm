# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapp(node):
            if not node: return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            swapp(node.left)
            swapp(node.right)
        swapp(root)
        return root
