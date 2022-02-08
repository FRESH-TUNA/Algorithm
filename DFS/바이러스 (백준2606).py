# https://www.acmicpc.net/problem/2606

from collections import defaultdict

def init():
    N, N_edges, edges = int(input()), int(input()), []
    while N_edges: 
        edges.append(list(map(int, input().split())))
        N_edges -= 1
    return edges

def make_graph(edges):
    graph = defaultdict(list)
    for (start, end) in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph

def dfs(edges, start, traced):
    answer = 1
    traced.add(start)
    for end in edges[start]: 
        if end not in traced: answer += dfs(edges, end, traced)
    return answer
    
# driver
print(dfs(make_graph(init()), 1, set()) - 1)