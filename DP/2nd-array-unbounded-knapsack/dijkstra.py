import heapq

def solution(sugar, salt, stuffs):
    MAX_SUGAR = max(s[0] for s in stuffs) 
    MAX_SALT = max(s[1] for s in stuffs)
    MAX_TIME = MAX_SUGAR + MAX_SALT
    stuffs = [[0,0,1,0,1], [0,0,0,1,1]] + stuffs
    DB = [[MAX_TIME for _ in range(MAX_SALT+1)] for _ in range(MAX_SUGAR+1)]
    Q = []
    
    # init
    for su in range(sugar+1):
        for sa in range(salt+1):
            DB[su][sa] = 0
    
    heapq.heappush(Q, (0, sugar, salt))

    while Q:
        d, x, y = heapq.heappop(Q)
        for rx, ry, dx, dy, dd in stuffs:
            if x < rx or y < ry: continue
            if x+dx > MAX_SUGAR or y+dy > MAX_SALT: continue
            if DB[x+dx][y+dy] > DB[x][y] + dd:
                DB[x+dx][y+dy] = DB[x][y] + dd
                heapq.heappush(Q, (DB[x+dx][y+dy], x+dx, y+dy))
    return DB[-1][-1]

# driver
a, c = 0, 0
s = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	

from itertools import permutations

for _s in permutations(s):
    print(solution(a, c, list(_s)))
