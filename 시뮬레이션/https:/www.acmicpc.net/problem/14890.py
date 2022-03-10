import sys

def solution(N, L, G):
    return calc(N, L, G) + calc(N, L, list(zip(*G)))

def calc(N, L, G):
    installed = [[0 for _ in range(N)] for _ in range(N)]
    res = 0

    for i in range(N):
        p, j, can_go = 0, 1, True
        while j < N:
            p_v, v = G[i][p], G[i][j]
            if v == p_v:
                p, j = p+1, j+1
                continue
            elif v > p_v:
                if not can_upper(L, G, i, p, j, installed):
                    can_go = False
                    break
                install(installed, i, j-L, j)
                p, j = p+1, j+1
            else:
                if not can_under(N, L, G, i, p, j, installed):
                    can_go = False
                    break
                install(installed, i, j, j+L)
                p, j = j+L-1, j+L
            if not can_go: break
        if can_go: res += 1
    return res

def can_upper(L, G, i, p, j, installed):
    p_v, v = G[i][p], G[i][j]
    if v-p_v > 1 or j-L < 0: return False
    for y in range(j-L, j):
        if G[i][y] != p_v or installed[i][y]: return False
    return True

def can_under(N, L, G, i, p, j, installed):
    p_v, v = G[i][p], G[i][j]
    if p_v-v > 1 or j+L-1 >= N: return False
    for y in range(j, j+L):
        if G[i][y] != v or installed[i][y]: return False
    return True

def install(installed, r, start, end):
    for i in range(start, end): installed[r][i] = 1
    
# driver
input = sys.stdin.readline
N, L = map(int, input().split())
G = [list(map(int, input().split()[:N])) for _ in range(N)]
print(solution(N, L, G))
