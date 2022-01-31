# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def _bstToGst(node: TreeNode, parent_r_sum):
            l_node, r_node = None, None
            l_sum, r_sum = 0, 0
            
            if node.right:
                r_node, r_sum = _bstToGst(node.right, parent_r_sum)
            if node.left:
                l_node, l_sum = _bstToGst(node.left, parent_r_sum+r_sum+node.val)
            
            new_node = TreeNode(node.val+r_sum+parent_r_sum, l_node, r_node)
            return (new_node, node.val+l_sum+r_sum)
        return _bstToGst(root, 0)[0]
