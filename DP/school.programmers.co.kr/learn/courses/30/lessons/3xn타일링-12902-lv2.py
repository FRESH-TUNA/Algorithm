def solution(n):
    N, DIVIDER = 5000, 1000000007
    DB, DB[2], DB[4] = [0]*(N+1), 3, 11
    
    for i in range(6, N+1, 2):
        DB[i] = (DB[i-2]*DB[2] + sum(DB[:i-2])*2 + 2) % DIVIDER
    return DB[n]

