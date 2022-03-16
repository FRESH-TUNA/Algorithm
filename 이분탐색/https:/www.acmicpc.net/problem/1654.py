import sys

# global
N, TARGET = 0, 0

def solution(LINES):
    min_res, max_res = 1, 2**31-1
    res = min_res

    while(min_res <= max_res):
        ans = min_res + (max_res-min_res) // 2
        if sum(l // ans for l in LINES) >= TARGET: 
            min_res = ans+1
            res = max(res, ans)
        else: max_res = ans-1
    return res

# driver
input = sys.stdin.readline
N, TARGET = map(int, input().split())
LINES = [int(input()) for _ in range(N)]
print(solution(LINES))
