class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, traced = collections.defaultdict(list), {}
        
        def dfs(trace, start):
            for end in graph[start]:
                if traced["".join((str(start), str(end)))]: continue
                traced["".join((str(start), str(end)))] = True
                
                if end in trace: return False
                trace.add(end)
                if not dfs(trace, end): return False
                trace.remove(end)
            return True

        for (i, j) in prerequisites: 
            graph[i].append(j)
            traced["".join((str(i), str(j)))] = False
            
        for (i, j) in prerequisites: 
            if traced["".join((str(i), str(j)))]: continue
            traced["".join((str(i), str(j)))] = True
            if i == j or not dfs({i, j}, j): return False
            
        return True
