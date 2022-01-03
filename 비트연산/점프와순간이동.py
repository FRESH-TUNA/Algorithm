def solution(n):
    answer = 0
    while n: 
        answer = answer + 1 if n % 2 else answer
        n = n - 1 if n % 2 else n // 2
    return answer
