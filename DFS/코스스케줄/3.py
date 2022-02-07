from collections import defaultdict

def solution(tickets):
    N = len(tickets) + 1
    graph, answer, stack = defaultdict(list), [], ["ICN"]
    
    for (s, e) in sorted(tickets, reverse=True):
        graph[s].append(e)

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())    
        answer.append(stack.pop())
    return answer[::-1]
