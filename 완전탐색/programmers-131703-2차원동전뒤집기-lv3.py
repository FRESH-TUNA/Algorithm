def solution(beginning, target):
    R, C = len(beginning), len(beginning[0])
    answer = 10000000000

    def correct(origin, c):
        for r in range(R):
            if origin[r][c] != target[r][c]:
                return False
        return True
    
    def reverseCorrect(origin, c):
        for r in range(R):
            if origin[r][c] == target[r][c]:
                return False
        return True
    
    def init(tmp, origin):
        for r in range(R):
            for c in range(C):
                tmp[r][c] = origin[r][c]

    # row
    for rowValue in range(1<<R):
        origin = [[c for c in row] for row in beginning]
        mr, mc = 0, 0
        
        for r in range(R):
            if (1<<r)&rowValue:
                mr += 1
                for c in range(C):
                    origin[r][c] = (0 if origin[r][c]==1 else 1) 

        if mr > answer:
            return answer
        
        for colValue in range(1<<C):
            mc = 0
            canAnswer = True
            for c in range(C):
                if (1<<c)&colValue:
                    if reverseCorrect(origin, c):
                        mc += 1
                    else:
                        canAnswer = False
                        break
                elif not correct(origin, c):
                    canAnswer = False
                    break
                    
            if canAnswer:
                answer = min(answer, mr+mc)
            else:
                continue
            
    return -1 if answer == 10000000000 else answer

