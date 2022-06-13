import sys
from collections import deque
from itertools import combinations

def solution(N, M, GRAPH):
    cities, stores = find_cities_and_stores(N, GRAPH)
    store_cases = combinations(stores, M)
    res = sys.maxsize
    for case in store_cases:
        res = min(res, distance(case, cities, res))
    return res

def distance(case, cities, max_res):
    cres = 0
    for (ci, cj) in cities:
        d = sys.maxsize
        for (si, sj) in case: 
            d = min(d, abs(ci-si) + abs(cj-sj))
        cres += d
        if cres >= max_res: return max_res     
    return cres

def find_cities_and_stores(N, GRAPH):
    cities, stores = [], []
    for i in range(N):
        for j in range(N):
            if GRAPH[i][j] == 1: cities.append((i, j))
            elif GRAPH[i][j] == 2: stores.append((i, j))
    return cities, stores

# driver
input = sys.stdin.readline
N, M = map(int, input().split())
GRAPH = [list(map(int, input().split()[:N]))
        for _ in range(N)]
print(solution(N, M, GRAPH))
