import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N = int(input())
    ORDER, PREFER = [0]*(N**2), [None]*(N**2)
    G = [[0 for _ in range(N)] for _ in range(N)]
    D, DR, DC = 4, (-1,0,1,0), (0,1,0,-1)

    def prefer_order_init():
        for i in range(N**2):
            j, b1, b2, b3, b4 = map(int, input().split())
            ORDER[i], PREFER[i] = j, {b1, b2, b3, b4}

    def call():
        print(first_step(0, PREFER[0]))
            
    def first_step(i, prefer):
        q, maxadj = list(), 0
        max_prefers = 0
        
        for r in range(N):
            for c in range(N):
                prefers = 0
                for d in range(D):
                    cr, cc = r+DR[d], c+DC[d]
                    if cr==-1 or cr==N or cc==-1 or cc==N:
                        continue
                    if G[cr][cc] in prefer:
                        prefers += 1
                if prefers > max_prefers:
                    prefers = max_prefers
                    q.clear()
                    q.append((r, c))
                elif prefers == max_prefers:
                    q.append((r, c))
        return q
    prefer_order_init()
    call()
solution()

