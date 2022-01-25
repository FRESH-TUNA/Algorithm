def solution(gems):
    db, answer, gems = {}, [1, 110000], ["dummy"] + gems
    MAX_GEMS = len(set(gems)) - 1
    
    for i in range(1, len(gems)):
        candid = {gems[i]}
        for j in range(i, len(gems)):
            candid.add(gems[j])
            if len(candid) == MAX_GEMS:
                answer = min(
                    answer, [i, j],
                    key=lambda x: x[1]-x[0])
    return answer
