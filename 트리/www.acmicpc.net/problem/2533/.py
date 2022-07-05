import sys

def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    G = [[] for _ in range(N+1)]
    DB = [[0, 0] for _ in range(N+1)]
    T = [0 for _ in range(N+1)]
    ADAPTER, NOT_ADAPTER = 0, 1

    def graph():
        for _ in range(N-1):
            a, b = map(int, input().split())
            G[a].append(b)
            G[b].append(a)
    def dfs(node):
        T[node], DB[node][ADAPTER] = 1, 1
        for new_node in G[node]:
            if not T[new_node]:
                dfs(new_node)
                DB[node][ADAPTER] += min(DB[new_node][ADAPTER], DB[new_node][NOT_ADAPTER])
                DB[node][NOT_ADAPTER] += DB[new_node][ADAPTER]
    def call():
        graph()
        dfs(1)
        print(min(DB[1][0], DB[1][1]))
    call()

solution()
