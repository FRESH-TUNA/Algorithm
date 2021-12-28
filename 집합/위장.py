from functools import reduce

def solution(clothes):
    db = {}
    for (name, _type) in clothes:
        if _type in db: db[_type] += 1
        else: db[_type] = 1
    return reduce(lambda a, c: a * c, [v + 1 for v in db.values()], 1) - 1
