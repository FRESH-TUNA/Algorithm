class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        
        ans, r_val = 0, root.val
        if r_val >= low and r_val <= high:
            ans += r_val + (
                self.rangeSumBST(root.left, low, high) + 
                self.rangeSumBST(root.right, low, high))
        elif r_val < low:
            ans += self.rangeSumBST(root.right, low, high)
        elif r_val > high:
            ans += self.rangeSumBST(root.left, low, high)
        
        return ans