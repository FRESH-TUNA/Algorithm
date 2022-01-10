def solution(n):
    cases, a = ['0', '1', '2'], []
    while n != 0:
        n, remain = n // 3, n % 3
        a.append(cases[remain])
    return sum(int(v) * (3 ** i) for i, v in enumerate(reversed(a)))
