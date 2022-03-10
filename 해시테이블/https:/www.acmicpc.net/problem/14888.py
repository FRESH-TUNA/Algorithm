import sys
from itertools import permutations
from collections import deque

def solution(NUMS, OP_CASES):
    max_ans, min_ans = -1000000000, 1000000000
    
    for case in OP_CASES:
        res = calculate(NUMS, case)
        max_ans = max(max_ans, res)    
        min_ans = min(min_ans, res)
    return str(max_ans), str(min_ans)

def calculate(NUMS, ops):
    Q = deque(NUMS)
    res = Q.popleft()

    for op in ops:
        right = Q.popleft()
        if op == 0: res += right
        elif op == 1: res -= right
        elif op == 2: res *= right
        elif res > 0: res = res // right
        else: res = (-1) * ((res * -1) // right)
    return res

def in_border(N, M, x, y):
    return not (x in (-1, N) or y in (-1, M))

# driver
input = sys.stdin.readline
N = int(input())
NUMS = list(map(int, input().split()))
OP_N = map(int, input().split()[:4])

OPS = []
for i, n in enumerate(OP_N): 
    if n: OPS.extend([i] * n)
print('\n'.join(solution(NUMS, set(permutations(OPS)))))
