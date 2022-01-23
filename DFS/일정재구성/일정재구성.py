#https://leetcode.com/problems/reconstruct-itinerary/submissions/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph, traced = {}, {}
        border = len(tickets)+1
        
        for (start, end) in tickets:
            if start in graph: graph[start].append(end)
            else: graph[start] = [end]
            if end not in graph: graph[end] = []

            edge_key = "".join((start, end))
            if edge_key in traced: traced[edge_key] += 1
            else: traced[edge_key] = 1
                
        for edges in graph: graph[edges].sort()
        
        return self.dfs(graph, traced, ["JFK"], border)
        
    
    def dfs(self, graph, traced, cur, border):
        if len(cur) == border: return cur

        start = cur[-1]
        for end in graph[start]:
            edge_key = "".join((start, end))
            if not traced[edge_key]: continue
            traced[edge_key] -= 1
            cur.append(end)
            
            res = self.dfs(graph, traced, cur, border)
            if res != None: return res

            traced[edge_key] += 1
            cur.pop()
            
        return None