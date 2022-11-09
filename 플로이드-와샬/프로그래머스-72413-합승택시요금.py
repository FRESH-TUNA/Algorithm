def solution(n, s, a, b, fares):
    MAX_FARE = 100000000000
    DISTS = [[MAX_FARE]*(n+1) for _ in range(n+1)]
    answer = MAX_FARE*3

    # graph
    for x, y, cost in fares:
        DISTS[x][y] = DISTS[y][x] = cost
    
    # dist init
    for i in range(1, n+1):
        DISTS[i][i] = 0

    # solution
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                DISTS[i][j] = min(DISTS[i][j], DISTS[i][k]+DISTS[k][j])
    
    for i in range(1, n+1):
        answer = min(answer, DISTS[s][i]+DISTS[i][a]+DISTS[i][b])
    
    return answer

