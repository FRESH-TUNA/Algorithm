import sys
from collections import defaultdict

def init():
    input = sys.stdin.readline
    CASE_N = int(input())
    NS, EDGES = [], []
    for _ in range(CASE_N):
        NS.append(int(input()))
        EDGES.append([input().rstrip().split() 
                      for _ in range(NS[-1])])
    return CASE_N, NS, EDGES

def solutions(CASE_N, NS, EDGES):
    for i in range(CASE_N): solution(NS[i], EDGES[i])

def solution(N, EDGES):
    ROOT, NODES = dict(), defaultdict(lambda: 1)
    for n1, n2 in EDGES:
        print(union(ROOT, NODES, n1, n2))

def union(ROOT, NODES, i, j):
    ps, pe = parent(ROOT, i), parent(ROOT, j)
    if ps == pe: return NODES[ps] 
    if pe > ps: 
        ROOT[pe] = ps
        NODES[ps] += (NODES[pe])
        return NODES[ps]
    else: 
        ROOT[ps] = pe
        NODES[pe] += (NODES[ps])
        return NODES[pe]

def parent(ROOT, n):
    pointer = n
    while pointer in ROOT: 
        ROOT[n] = pointer = ROOT[pointer]
    return pointer

if __name__ == '__main__':
    solutions(*init())
