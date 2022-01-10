def solution(d, budget, answer=0):
    for x in sorted(d):
        if x > budget: return answer
        answer, budget = answer+1, budget-x
    return answer
