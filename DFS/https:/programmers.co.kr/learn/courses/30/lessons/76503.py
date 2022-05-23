from collections import defaultdict
import sys

sys.setrecursionlimit(300000)
Traced = []
Answer = 0

def solution(a, edges):
    global Traced
    if sum(a) != 0: return -1

    Traced = [0] * len(a)

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    dfs(0, graph, a)
    return Answer

def dfs(node, graph, a):
    global Answer
    Traced[node] = 1
    for connected in graph[node]:
        if not Traced[connected]:
            a[node] += dfs(connected, graph, a)
    Answer += abs(a[node])
    return a[node]
