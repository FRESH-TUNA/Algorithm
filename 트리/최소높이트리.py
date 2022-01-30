class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1: return [0]
        
        graph = collections.defaultdict(list)
        
        for (s, e) in edges:
            graph[s].append(e)
            graph[e].append(s)
            
        leaves = []
        for x in graph:
            if len(graph[x]) == 1: leaves.append(x)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                end = graph[leaf].pop()
                graph[end].remove(leaf)
                if len(graph[end]) == 1:
                    new_leaves.append(end)
            leaves = new_leaves
        return leaves
