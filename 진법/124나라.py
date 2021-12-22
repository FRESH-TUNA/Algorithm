# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    result = ''
    values = ['4', '1', '2']
    
    # python은 0, 1로 while 평가 가능
    while n:
        n, remain = n // 3, n % 3
        if remain == 0: n = n - 1
        result = values[remain] + result
    return result
