def solution(s, n = 0):
    for c in s:
        if c == ")" and not n: return False
        n += 1 if c == "(" else -1
    return False if n else True
