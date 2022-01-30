# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:    
    def _serialize(self, nodes, root, idx):
        if not root: return
        
        l_idx = 2*idx+1 if root.left else "X"
        r_idx = 2*(idx+1) if root.right else "X"
        
        nodes.append(",".join(
            map(str, (idx, root.val, l_idx, r_idx))))
    
        if root.left: self._serialize(nodes, root.left, l_idx)
        if root.right: self._serialize(nodes, root.right, r_idx)
        

    def serialize(self, root):
        nodes = []
        self._serialize(nodes, root, 0)
        return "|".join(nodes)
        
    def _deserialize(self, graph, idx):
        r_v, l_idx, r_idx = graph[idx]
        root = TreeNode(int(r_v))
        
        if l_idx is not None:
            root.left = self._deserialize(graph, l_idx)
        if r_idx is not None:
            root.right = self._deserialize(graph, r_idx)
        return root
    
    def deserialize(self, data):
        if not data: return None
        
        graph, data = {}, data.split("|")
        for d in data:   
            idx, r_v, l_idx, r_idx = d.split(",")
            graph[idx] = (
                r_v, 
                None if l_idx == "X" else l_idx,
                None if r_idx == "X" else r_idx )
        return self._deserialize(graph, next(iter(graph)))
