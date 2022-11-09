def solution(distance, scope, times):
    scope = [[s[1], s[0]] if s[0]>s[1] else s for s in scope]

    for (start, end), (work, rest) in sorted(zip(scope, times)):
        circulation = work+rest

        for pos in range(start-1, end):
            if pos%circulation < work:
                return pos+1
    return distance

