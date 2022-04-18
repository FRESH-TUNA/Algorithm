import sys

def init():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    EDGES = [list(map(int, input().rstrip().split())) 
             for _ in range(M)]
    return N, M, EDGES

def solution(N, M, EDGES):
    ROOT = [i for i in range(N)]
    
    for i in range(M):
        s, e = min(EDGES[i]), max(EDGES[i])
        ps, pe = parent(ROOT, s), parent(ROOT, e)
        if ps == pe:
            print(i+1)
            return
        if pe > ps: ROOT[pe] = ps
        else: ROOT[ps] = pe
    print(0)

def parent(ROOT, n):
    pointer = n
    while ROOT[pointer] != pointer: 
        ROOT[n] = pointer = ROOT[pointer]
    return pointer

if __name__ == '__main__':
    solution(*init())
