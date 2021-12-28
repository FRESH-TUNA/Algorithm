import bisect as bi

def solution(citations):
    h, c = 0, sorted(citations)
    while h + 1 <= len(c):
        i = bi.bisect_left(c, h + 1)
        if not (len(c[i:]) >= h + 1 and len(c[:i]) <= h + 1): return h
        h += 1  
    return len(c)
