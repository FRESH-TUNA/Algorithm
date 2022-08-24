from sys import stdin
import sys

def solution(num):
    N = len(num)
    ans = [0] * N
    helper = [int(num[i:i+2]) for i in range(N-1)] + [27]
    return dfs(num, 0, ans, helper)

def dfs(num, i, ans, helper):
    if i == len(num): return 1
    if ans[i]: return ans[i]

    # 1이상 검사
    if num[i] != '0':
        ans[i] += dfs(num, i+1, ans, helper)

    # 10이상 검사
    if 10 <= helper[i] <= 26:
        ans[i] += dfs(num, i+2, ans, helper)

    ans[i] %= 1000000
    return ans[i]
    
# driver
sys.setrecursionlimit(10000) 
print(solution(stdin.readline()))
