from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
G = [[] for _ in range(N+1)]

def graph():
    for _ in range(N-1):
        a, b, usado = (map(int, input().split()))
        G[a].append((b, usado))
        G[b].append((a, usado))

def call():
    for i in range(Q):
        k, v = map(int, input().split())
        visited, visited[v], result = [0]*(N+1), 1, 0
        q = deque()
        
        q.append((v, float('inf')))

        while q:
            v, usado = q.pop()
            for nv, nusado in G[v]:
                nusado = min(usado, nusado)
                if nusado >= k and not visited[nv]:
                    result += 1
                    q.append((nv, nusado))
                    visited[nv] = True
        print(result)

graph()
call()
