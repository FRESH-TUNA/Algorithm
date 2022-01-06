def solution(n):
    _n, answer, last_n = 1, 1, n // 2
    while _n <= last_n:
        if determine(_n, n): answer += 1
        _n += 1
    return answer

def determine(n, origin):
    _n, idx = n, 1
    while _n < origin: 
        _n += n + idx
        idx += 1
    return _n == origin
