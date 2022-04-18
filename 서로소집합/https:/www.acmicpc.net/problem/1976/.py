import sys

def init():
    input = sys.stdin.readline
    N, M = int(input()), int(input())
    EDGES = [list(map(int, input().rstrip().split())) 
             for _ in range(N)]

    PLAN = list(map(int, input().rstrip().split()))
    
    return N, M, EDGES, PLAN

def solution(N, M, EDGES, PLAN):
    ROOT = [i for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if EDGES[i][j]: union(ROOT, i, j)

    prev = parent(ROOT, PLAN[0]-1)
    for c in PLAN[1:]:
        next_prev = parent(ROOT, c-1)
        if next_prev != prev:
            print("NO")
            return
        prev = next_prev
    print("YES")

def union(ROOT, i, j):
    ps, pe = parent(ROOT, i), parent(ROOT, j)
    if pe > ps: ROOT[pe] = ps
    else: ROOT[ps] = pe

def parent(ROOT, n):
    pointer = n
    while ROOT[pointer] != pointer: 
        ROOT[n] = pointer = ROOT[pointer]
    return pointer

if __name__ == '__main__':
    solution(*init())