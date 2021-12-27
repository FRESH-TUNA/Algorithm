from itertools import product
from bisect import bisect_left

def insert_into_db(db, infos):
    cases = list(product((0, 1), repeat=4))
    for info in infos:
        spec, score = info[:4], info[-1]
        for case in cases:
            key = "".join([spec[i] if v else "-" for i, v in enumerate(case)])
            if key not in db: db[key] = [int(score)]
            else: db[key].append(int(score))

def querying(db, query):
    key = "".join(query[::2])
    if not key in db: return 0
    datas = db[key]
    return len(datas) - bisect_left(datas, int(query[-1]))

def solution(info, query):
    infos, queries = [i.split() for i in info], [q.split() for q in query]
    infos.sort(key=lambda x: int(x[-1]))
    db = {}
    insert_into_db(db, infos)
    return [querying(db, q) for q in queries]
