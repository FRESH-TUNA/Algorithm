import sys

input = sys.stdin.readline

N, M = 0, 0

def dfs(stack, c, last_v):
    if c == M:
        print(*stack)
        return
    for i in range(last_v, N+1):
        stack.append(i)
        dfs(stack, c+1, i+1)
        stack.pop()

# driver
N, M = map(int, input().split())
dfs([], 0, 1)
