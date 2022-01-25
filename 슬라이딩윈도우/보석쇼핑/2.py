from collections import defaultdict
def solution(gems):
    ans, db = [1, 100001], defaultdict(lambda: 0)
    gems = ["dummy"] + gems
    start, end, MAX_GEMS = 1, 1, len(set(gems)) - 1
    
    while True:
        if start == len(gems): break
        if len(db) == MAX_GEMS:
            ans = min(ans, [start, end-1], 
                      key=lambda x: x[1]-x[0])
            db[gems[start]] -= 1
            if not db[gems[start]]: del db[gems[start]]
            start += 1
            continue
        if end == len(gems): break
        if len(db) != MAX_GEMS:
            db[gems[end]] += 1
            end += 1
            continue

    return ans
