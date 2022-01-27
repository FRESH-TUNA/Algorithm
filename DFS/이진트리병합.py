class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        
        return TreeNode(
            (root1.val if root1 else 0) + (root2.val if root2 else 0),
            self.mergeTrees(root1.left if root1 else None, 
                            root2.left if root2 else None),
            self.mergeTrees(root1.right if root1 else None, 
                            root2.right if root2 else None)
        )
