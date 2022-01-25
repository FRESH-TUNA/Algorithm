class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue, l = collections.deque(((1, root),)), 1
        
        if not root: return 0
        
        while queue:
            _l, node = queue.pop()
            l = max(_l, l)
            if node.left: queue.appendleft((_l+1, node.left))
            if node.right: queue.appendleft((_l+1, node.right))
            
        return l
