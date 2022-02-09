OUTBOUNDS = (-1, 3)

def dfs(i, j, graph, paths, stack):
    cases = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for (ni, nj) in cases:
        if ni in OUTBOUNDS or nj in OUTBOUNDS: continue
        if not graph[ni][nj]: continue
        
        v = graph[ni][nj]
        stack.append(graph[ni][nj])
        graph[ni][nj] = 0
        
        if ni == 2 and nj == 2: 
            paths.append([x for x in stack])
        
        dfs(ni, nj, graph, paths, stack)
        graph[ni][nj] = v
        stack.pop()

graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
traced, paths, stack = set(), [], [1]
graph[0][0] = 0 

dfs(0, 0, graph, paths, stack)
for path in paths: print(path)