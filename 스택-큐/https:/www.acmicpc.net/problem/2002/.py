import sys
from collections import deque

# global
N, IN, OUT = 0, deque(), []

def init():
    global N
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N): IN.append(input().rstrip())
    for _ in range(N): OUT.append(input().rstrip())

def main():
    traced = set()
    res = 0

    for word in OUT:        
        while IN and IN[0] in traced: IN.popleft()
        if word != IN[0]: res += 1
        traced.add(word)
    print(res)
        
        
# driver
init()
main()
