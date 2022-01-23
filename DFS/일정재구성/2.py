class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph, ans = collections.defaultdict(list), []
        for s, e in sorted(tickets, reverse=True): 
            graph[s].append(e)
        
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            ans.append(start)
            
        dfs('JFK')
        return ans[::-1]
