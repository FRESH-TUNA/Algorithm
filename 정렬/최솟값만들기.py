from functools import reduce

def solution(A,B):
    Z = zip(sorted(A), sorted(B, reverse=True))
    return reduce(lambda a, c: a + c[0]*c[1], Z, 0)
