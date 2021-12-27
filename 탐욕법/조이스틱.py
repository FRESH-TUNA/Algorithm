def solution(name):
    name = list(name)
    shifted = 0
    min_traced = len(name) - 1
    
    for idx, c in enumerate(name):
        shifted += min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)    
        next_A_idx = idx + 1
        
        while next_A_idx < len(name) and name[next_A_idx] == "A":
            next_A_idx += 1
        
        min_traced = min(min_traced, idx * 2 + len(name) - next_A_idx)

    return min_traced + shifted
