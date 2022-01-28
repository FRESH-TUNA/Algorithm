# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0

            _ans = [0]
            l_ans, r_ans = dfs(node.left), dfs(node.right)

            if node.left and node.left.val == node.val:
                _ans.append(l_ans+1)
            if node.right and node.right.val == node.val:
                _ans.append(r_ans+1)

            self.ans = max(sum(_ans), self.ans)
            return max(_ans)
        
        dfs(root)
        return self.ans
                