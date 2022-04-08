N = int(input())
RES = 0
COL_T = [0]*N
SLASH_T, BACKSLASH_T = [0]*(2*N-1), [0]*(2*N-1)

def dfs(r):
    global RES
    if r == N:
        RES += 1
        return
    else:
        for c in range(N):
            if COL_T[c] or BACKSLASH_T[r-c+N-1] or SLASH_T[r+c]: continue
            COL_T[c] = BACKSLASH_T[r-c+N-1] = SLASH_T[r+c] = 1
            dfs(r+1)
            COL_T[c] = BACKSLASH_T[r-c+N-1] = SLASH_T[r+c] = 0
dfs(0)
print(RES)
