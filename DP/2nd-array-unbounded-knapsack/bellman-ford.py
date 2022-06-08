def solution(sugar, salt, stuffs):
    print(stuffs)
    MAX_SUGAR = max(s[0] for s in stuffs) 
    MAX_SALT = max(s[1] for s in stuffs)
    MAX_TIME = MAX_SUGAR + MAX_SALT
    stuffs = [[0,0,1,0,1], [0,0,0,1,1]] + stuffs
    DB = [[MAX_TIME for _ in range(MAX_SALT+1)] for _ in range(MAX_SUGAR+1)]

    # init
    for su in range(sugar+1):
        for sa in range(salt+1):
            DB[su][sa] = 0

    for _ in range(len(stuffs)):
        for rSugar, rSalt, dSugar, dSalt, time in stuffs:
            for su in range(MAX_SUGAR+1):
                for sa in range(MAX_SALT+1):
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
a, c = 0, 0
s = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

from itertools import permutations

for _s in permutations(s):
    print(solution(a, c, list(_s)))
