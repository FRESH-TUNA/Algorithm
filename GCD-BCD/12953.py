# programmers
# N개의 최소공배수

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for n in arr[1:]:
        answer = lcm(answer, n)
    return answer
