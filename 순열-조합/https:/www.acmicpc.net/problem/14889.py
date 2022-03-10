import sys
from itertools import permutations, combinations

def solution(N, GRAPH):
    TEAMS = combinations(range(N), N // 2)
    res = 100 * N * N
    
    for TEAM in TEAMS:
        res = min(res, difference(N, GRAPH, TEAM))
    return res

def difference(N, GRAPH, TEAM):
    B_TEAM = set(range(N)) - set(TEAM)
    res = sum(GRAPH[x][y] for (x, y) in permutations(TEAM, 2))
    b_res = sum(GRAPH[x][y] for (x, y) in permutations(B_TEAM, 2))
    return abs(res - b_res)

    
# driver
input = sys.stdin.readline
N = int(input())
GRAPH = [list(map(int, input().split()[:N])) for _ in range(N)]
print(solution(N, GRAPH))
