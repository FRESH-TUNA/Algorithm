def solution(key, lock):
    R, C = len(lock), len(lock[0])
    HOLE = set()
    Lock = [[0 for _ in range(C*3)] for _ in range(R*3)]
    
    for r in range(R):
        for c in range(C):
            Lock[r+R][c+C] = lock[r][c]
            if not lock[r][c]:
                HOLE.add((r+R, c+C))

    def check(r, c, keyR, keyC, key):
        res = set()
        for k in range(keyR):
            for l in range(keyC):
                if key[k][l] and Lock[r+k][c+l]:
                    return False
                elif key[k][l] or Lock[r+k][c+l]:
                    res.add((r+k, c+l))
        return (res >= HOLE)
    
    for _ in range(4):
        key = list(zip(*[row[::-1] for row in key]))
        keyR, keyC = len(key), len(key[0])
        
        for i in range(3*R-keyR+1):
            for j in range(3*C-keyC+1):
                if check(i, j, keyR, keyC, key):
                    return True
                            
    return False
