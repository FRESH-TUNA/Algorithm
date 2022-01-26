from collections import defaultdict
from collections import Counter

def solution(gems):
    MAX_GEMS, buys = len(set(gems)), Counter()
    start, end, is_end = 1, 1, True
    gems, ans = ["dummy"] + gems, [1, 100001]

    while True:
        if is_end:
            if end == len(gems): break
            else: buys[gems[end]] += 1
            
            if len(buys) == MAX_GEMS: 
                is_end = False
                ans = update(ans, [start, end])
            end += 1 
        else:
            if start == len(gems): break
            
            if buys[gems[start]] == 1: 
                del buys[gems[start]]
            else: buys[gems[start]] -= 1
            
            start += 1 
            
            if len(buys) != MAX_GEMS: is_end = True
            else: ans = update(ans, [start, end-1])    

    return ans

def update(ans, candid):
    return min(ans, candid, key=lambda x: x[1]-x[0])
