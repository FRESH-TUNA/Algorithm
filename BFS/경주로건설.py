from collections import deque

def solution(board):
    N, Q = len(board), deque([(0,0,-1,0)])
    MAX_DIST = 100000000
    OUTBOUNDS, UNREACHABLE = (N, -1), 1
    
    dists = [[MAX_DIST for _ in range(N)] for _ in range(N)]
    answer = MAX_DIST
    
    while Q:
        y, x, d, c = Q.pop()

        if (y, x) == (N-1, N-1): 
            answer = min(answer, c)

        cases = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
        for direction, (ny, nx) in enumerate(cases):            
            if ny in OUTBOUNDS or nx in OUTBOUNDS: continue
            if board[ny][nx] == UNREACHABLE: continue

            cost = c + (100 if d == direction else 600)
    
            if dists[ny][nx] < cost - 400: continue
                
            Q.appendleft((ny, nx, direction, cost))
            dists[ny][nx] = cost

    return answer - 500
