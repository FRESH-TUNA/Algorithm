def solution(name):
    answer = 0
    min_lr_shifted = len(name) - 1
    
    for i, v in enumerate(name):
        # 상하
        answer += min(ord(v) - ord("A"), ord("Z") - ord(v) + 1)
        
        # 좌우 최소 계산
        next_i = i
        while next_i + 1 < len(name) and name[next_i + 1] == "A":
            next_i += 1
        
        min_lr_shifted = min(min_lr_shifted, i + i + len(name) - next_i - 1)
            
    return answer + min_lr_shifted
