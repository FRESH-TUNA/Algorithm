import sys
from collections import deque

def solution(n, seq, p, dq):
    res = 1
    while dq:
        if dq[0][1] == p[-1]:
            if dq[0][0] == seq: return res
            dq.popleft()
            p.pop()
            res += 1
        else: dq.append(dq.popleft())

# driver
input = sys.stdin.readline
for _ in range(int(input())):
    n, seq = map(int, input().split())
    p = list(map(int, input().split()))
    dq = deque((i, v) for i, v in enumerate(p))
    print(solution(n, seq, sorted(p), dq))
