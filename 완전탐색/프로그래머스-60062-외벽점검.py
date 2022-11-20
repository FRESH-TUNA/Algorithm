from itertools import permutations


def solution(n, weak, dist):
    WEAK_N = len(weak)
    answer = float("inf")
    weak = weak + [w+n for w in weak]
    cases = list(permutations(dist))

    for i, start in enumerate(weak[:WEAK_N]):
        for dists in cases:

            pos, count, target = start, 0, weak[i+WEAK_N-1]
            for dist in dists:
                pos += dist
                count += 1
            
                if pos >= target:
                    answer = min(answer, count)
                    break
                else:
                    pos = [w for w in weak[i+1:i+WEAK_N] if w > pos][0]

    return -1 if answer == float("inf") else answer

