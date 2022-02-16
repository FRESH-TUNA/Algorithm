# https://sangsangss.tistory.com/199

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX_INDEX = 100
    itemX, itemY = itemX*2, itemY*2
    traced = [[1] * (MAX_INDEX+1) for _ in range(MAX_INDEX+1)]
    Q = deque()
    
    for (x1, y1, x2, y2) in rectangle:
        for x in range(2 * x1, 2 * x2 + 1):
            for y in range(2 * y1, 2 * y2 + 1): traced[x][y] = 0

    for (x1, y1, x2, y2) in rectangle:
        for x in range(2 * x1 + 1, 2 * x2):
            for y in range(2 * y1 + 1, 2 * y2): traced[x][y] = 1
            
    traced[characterX*2][characterY*2] = 1
    Q.append((characterX*2, characterY*2, 0))
    
    while Q:
        x, y, d = Q.pop()
        nexts = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        d += 1
        
        for (x, y) in nexts:
            if x in (-1, MAX_INDEX+1) or y in (-1, MAX_INDEX+1):
                continue
            if traced[x][y]: continue
            if (x, y) == (itemX, itemY):
                return d // 2
            
            traced[x][y] = 1
            Q.appendleft((x, y, d))
