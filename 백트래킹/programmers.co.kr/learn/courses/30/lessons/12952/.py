def solution(n):
    SLASH, BACKSLASH = [0] * (2*n+1), [0] * (2*n+1)
    COL = [0]*n
    answer, GET = [0], 0
    
    def dfs(row, queens):
        if row == n:
            answer[GET] += [0, 1][queens == n]
            return
        for col in range(n):
            slash, backslash = row+col, row-col+n
            if SLASH[slash] or BACKSLASH[backslash] or COL[col]:
                continue
            BACKSLASH[backslash] = COL[col] = SLASH[slash] = 1
            dfs(row+1, queens+1)
            BACKSLASH[backslash] = COL[col] = SLASH[slash] = 0
    dfs(0, 0)
    return answer[GET]
