def solution(a, b):
    return [[_x + _y for (_x, _y) in zip(x, y)] for (x, y) in zip(a, b)]
