from collections import Counter

def solution(gems):
    MAX_GEMS = len(set(gems))
    db = Counter()
    start, end = 0, len(gems)
    left = 0
    
    for right, value in enumerate(gems, 1):
        db[value] += 1
        
        while left < right and len(db) == MAX_GEMS:
            if end - start > right - left:
                start, end = left, right
            db[gems[left]] -= 1
            if not db[gems[left]]: del db[gems[left]]
            left += 1
            
    return [start+1, end]
