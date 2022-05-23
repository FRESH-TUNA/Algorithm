from collections import defaultdict, deque

def solution(a, edges):
    answer = 0
    graph = defaultdict(set)
    leaves = deque()
    
    if sum(a) != 0: return -1

    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    for node in graph:
        if len(graph[node]) == 1:
            leaves.append(node)
    
    while leaves:
        leaf = leaves.pop()

        if not graph[leaf]: return answer
    
        parent = next(iter(graph[leaf]))
        answer += abs(a[leaf])
        a[parent] += a[leaf]
        graph[parent].remove(leaf)

        if len(graph[parent]) == 1: leaves.appendleft(parent)
        
    return answer
