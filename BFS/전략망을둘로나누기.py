# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    # graph 만들기
    answer, graph = n, [[] for _ in range(n+1)]

    for (x, y) in wires: 
        graph[x].append(y)
        graph[y].append(x)
    
    for (x, y) in wires:
        traced = [0] * (n+1)
        traced[x], traced[y] = 1, 1
        answer = min(answer, abs(
            bfs(x, graph, traced) - bfs(y, graph, traced)))

    return answer

def bfs(start, graph, traced):
    answer, q = 0, deque([start])
    
    while q:
        answer += 1
        for x in graph[q.pop()]:
            if traced[x]: continue
            traced[x] = 1
            q.appendleft(x)
            
    return answer
