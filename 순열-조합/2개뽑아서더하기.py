from itertools import combinations
def solution(ns):
    return sorted(set(sum(x) for x in combinations(ns, 2)))
