import sys

# global
input = sys.stdin.readline
START, TARGET, RES = 0, 0, 1000000000 

def dfs(v, c):
    global RES
    if v > TARGET: return
    elif v == TARGET: 
        RES = min(RES, c)
        return
    else:
        dfs(v*10+1, c+1)
        dfs(v*2, c+1)

# driver
START, TARGET = map(int, input().split())
dfs(START, 0)
print(-1 if RES == 1000000000 else RES+1)
