import heapq

def solution(alp, cop, problems):
    targetAlp, targetCop = max(p[0] for p in problems), max(p[1] for p in problems)
    MAX_COST = 300
    DB = [[MAX_COST]*(targetCop+1) for _ in range(targetAlp+1)]
    problems += [[0,0,1,0,1], [0,0,0,1,1]]
    
    DB[min(targetAlp, alp)][min(targetCop, cop)] = 0
    Q = []
    heapq.heappush(Q, (0, min(targetAlp, alp), min(targetCop, cop)))
    
    while Q:
        cost, a, c = heapq.heappop(Q)
        
        if cost > DB[a][c]:
            continue

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if a<alp_req or c<cop_req:
                continue
            na, nc = min(a+alp_rwd, targetAlp), min(c+cop_rwd, targetCop)

            if DB[na][nc] > DB[a][c]+cost:
                DB[na][nc] = DB[a][c]+cost
                heapq.heappush(Q, (DB[na][nc], na, nc))
    return DB[-1][-1]

