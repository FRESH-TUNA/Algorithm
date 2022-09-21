# Unbounded knapsack strategy

def solution(alp, cop, problems):
    targetAlp, targetCop = max(p[0] for p in problems), max(p[1] for p in problems)
    MAX_COST = 300
    DB = [[MAX_COST]*(targetCop+1) for _ in range(targetAlp+1)]
    problems += [[0,0,1,0,1], [0,0,0,1,1]]
    
    for a in range(min(targetAlp, alp), targetAlp+1):
        for c in range(min(targetCop, cop), targetCop+1):
            if a<=alp and c<=cop:
                DB[a][c] = 0

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a<alp_req or c<cop_req:
                    continue
                na, nc = min(targetAlp, a+alp_rwd), min(targetCop, c+cop_rwd)
                DB[na][nc] = min(DB[na][nc], DB[a][c]+cost)
    return DB[-1][-1]

