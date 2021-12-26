def solution(N, A, B):
    _round = 1
    while True:
        A, B = [case // 2 + 1 if case % 2 else case // 2 for case in [A, B]]
        if A == B: return _round
        _round += 1
