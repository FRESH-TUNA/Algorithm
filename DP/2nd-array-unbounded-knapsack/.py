def solution(sugar, salt, stuffs):
    print(stuffs)
    MAX_SUGAR = max(s[0] for s in stuffs) 
    MAX_SALT = max(s[1] for s in stuffs)
    MAX_TIME = MAX_SUGAR + MAX_SALT
    stuffs = [[0,0,1,0,1], [0,0,0,1,1]] + stuffs
    N = len(stuffs)
    DB = [[MAX_TIME for _ in range(MAX_SALT+1)] for _ in range(MAX_SUGAR+1)]

    # init
    for su in range(sugar+1):
        for sa in range(salt+1):
            DB[su][sa] = 0
    
    for su in range(MAX_SUGAR+1):
        for sa in range(MAX_SALT+1):
            for rSugar, rSalt, dSugar, dSalt, time in stuffs:
                prevSu, prevSa = su-dSugar, sa-dSalt
                if prevSu < rSugar or prevSa < rSalt:
                    continue
                else:
                    DB[su][sa] = min(
                        DB[su][sa],
                        DB[prevSu][prevSa]+time,
                    )
    return DB[-1][-1]

# driver
a, c = 10, 10
s = [[10,15,2,1,2],[20,20,3,3,4]]

from itertools import permutations

for _s in permutations(s):
    print(solution(a, c, list(_s)))