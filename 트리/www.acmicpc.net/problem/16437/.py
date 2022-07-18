import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N+1)]
    TYPE, TRACED, C = [None]*(N+1), [0]*(N+1), [0]*(N+1)
    sys.setrecursionlimit(130000)
    
    def init_G():
        for n in range(2, N+1):
            t, a, p = input().split()
            TYPE[n], C[n] = t, int(a)
            G[n].append(int(p))
            G[int(p)].append(n)
        TYPE[1] = 'S'

    def dfs(node):
        res = 0
        TRACED[node] = 1
        
        for child in G[node]:
            res += 0 if TRACED[child] else dfs(child)
        res += C[node] * [-1,1][TYPE[node] == 'S']
        return [res, 0][res < 0]

    init_G()
    return dfs(1)
    
print(solution())
