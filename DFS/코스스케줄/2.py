from collections import defaultdict

def solution(tickets):
    N = len(tickets) + 1
    graph, answer = defaultdict(list), []
    
    for (s, e) in sorted(tickets, reverse=True):
        graph[s].append(e)

    dfs(graph, answer, "ICN")
    return answer[::-1]

def dfs(edges, answer, node):
    while edges[node]: 
        dfs(edges, answer, edges[node].pop())
    answer.append(node)
    