# https://www.acmicpc.net/problem/2133

from sys import stdin
def solution(N):
    if N & 1: return 0
    ans, ans[0], ans[2] = [0] * (N+1), 1, 3
    for i in range(4, N+1, 2):
        ans[i] += ans[i-2] * ans[2]
        for j in range(i-4, -1, -2): ans[i] += ans[j] * 2
    return ans[N]

# driver
print(solution(int(stdin.readline())))
