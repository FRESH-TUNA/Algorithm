# https://gurumee92.tistory.com/164
from itertools import product

def solution(N, number):
    db = [None] + [set((int(str(N) * n),)) for n in range(1, 8+1)]

    for answer in range(1, 8):
        if number in db[answer]: return answer
        for x in range(1, answer + 1):
            db[answer+1] |= get_new_cases(db[x], db[answer+1-x])

    return 8 if number in db[8] else -1

def get_new_cases(db_i, db_j):
    new_db = set()
    for (i, j) in product(db_i, db_j):
        cases = [i + j, i * j]
        if i >= j: cases.append(i - j)
        if j > 0: cases.append(i // j)
        new_db |= set(cases)
    return new_db
