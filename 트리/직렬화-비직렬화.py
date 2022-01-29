# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:    
    def _serialize(self, nodes, root, level, idx):
        if idx >= len(nodes):
            nodes.extend(["x" for _ in range(2**(level-1))]) 
        nodes[idx] = str(root.val)
        
        if root.left: self._serialize(nodes, root.left, level+1, idx*2+1)
        if root.right: self._serialize(nodes, root.right, level+1, 2*(idx+1))

    def serialize(self, root):
        if not root: return ""
        nodes = ["x"]
        self._serialize(nodes, root, 1, 0)
        return ",".join(nodes)
        
    def _deserialize(self, nodes, idx):
        root = TreeNode(int(nodes[idx]))
        
        if idx*2+1 < len(nodes) and nodes[idx*2+1] != "x":
            root.left = self._deserialize(nodes, idx*2+1)
        if 2*(idx+1) < len(nodes) and nodes[2*(idx+1)] != "x":
            root.right = self._deserialize(nodes, 2*(idx+1))
        return root
    
    def deserialize(self, data):
        if not data: return None
        else: return self._deserialize(data.split(","), 0)
        