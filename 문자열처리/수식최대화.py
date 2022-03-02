from itertools import permutations

def solution(expression):
    ans = 0
    for ops in permutations(('+', '-', '*'), 3):
        last, mid = ops[0], ops[1]
        changed_tokens = []
        for mid_tokens in expression.split(last):
            first_tokens = [f"({i})" for i in mid_tokens.split(mid)]
            changed_tokens.append(f'({mid.join(first_tokens)})')
        ans = max(ans, abs(eval(last.join(changed_tokens))))   
    return ans
