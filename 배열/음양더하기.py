def solution(absolutes, signs):
    return sum([a if s else a * -1 for (a, s) in zip(absolutes, signs)])
