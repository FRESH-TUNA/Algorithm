import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    T = int(input())
    
    def tree():
        n = int(input())
        t = [i for i in range(n+1)]
        
        for parent, child in [map(int, input().split()) for _ in range(n-1)]:
            t[child] = parent
        return t

    def nca(tree, a, b):
        parents = set()

        while tree[a] != a:
            parents.add(a)
            a = tree[a]
        parents.add(a)

        while tree[b] != b:
            if b in parents:
                return b
            b = tree[b]
        return b

    def call():
        for _ in range(T):
            print(nca(tree(), *map(int, input().split())))
    call()

solution()
