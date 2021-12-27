from itertools import combinations

def solution(relation):
    row_num, col_num = len(relation), len(relation[0])
    uniques, cases = [], []

    for i in range(1, col_num + 1):
        cases.extend(combinations(range(col_num), i))

    for case in cases:
        db = {tuple([item[key] for key in case]) for item in relation}
        if len(db) != row_num: continue
    
        is_unique = True
        for u_case in uniques:
            if u_case.issubset(set(case)): 
                is_unique = False
                break

        if is_unique: uniques.append(set(case))

    return len(uniques)
