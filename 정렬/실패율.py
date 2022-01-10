from functools import cmp_to_key

def solution(N, stages):
    none_cleared, reached = [0] * (N + 2), [0] * (N + 2)

    for stage in stages:
        none_cleared[stage] += 1
        while stage > 0:
            reached[stage], stage = reached[stage]+1, stage-1

    return sorted(range(N, 0, -1), 
        key=cmp_to_key(lambda x, y: compare(
            x, y, none_cleared, reached)))

def compare(x, y, none_cleared, reached):
    x_v = 0 if not reached[x] else none_cleared[x] / reached[x]
    y_v = 0 if not reached[y] else none_cleared[y] / reached[y]
    return y_v - x_v if x_v != y_v else x - y

