# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    numbers = ['4', '1', '2']
    answer = ''
    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer
