# 0 1 2 3 4 5 6 7 
# 0 1 2 3 0 1 2 3
# i%m+1 == p
def solution(n, t, m, p):
    logs, current = ["0"], 1
    while len(logs) // m < t + 1:
        logs.extend(transform(current, n))
        current += 1
    return "".join([l for i, l in enumerate(logs) if i%m+1 == p][:t])

# 진법변환 함수
def transform(n, jinbub):
    maps, answer = "0123456789ABCDEF", ''
    while n > 0:
        n, remain = n // jinbub, n % jinbub
        answer = maps[remain] + answer
    return answer
