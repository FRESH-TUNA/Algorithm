N = int(input())
RES = 0
TRACED = [0] * N

def valid(r):
    for i in range(r):
        if (TRACED[r] == TRACED[i] or 
           abs(TRACED[r] - TRACED[i]) == abs(r-i)):
            return False
    return True

def dfs(r):
    global RES
    if r == N:
        RES += 1
        return
    else:
        for c in range(N):
            TRACED[r] = c
            if valid(r): dfs(r+1)

dfs(0)
print(RES)
