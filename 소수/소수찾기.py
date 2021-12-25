https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2)) 

    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


####
from itertools import permutations
from functools import reduce
import math

def is_prime_number(x):
    if x in (0, 1): return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    answer, cases = 0, set()
    
    for i in range(1, len(numbers) + 1):
        cases |= set([int("".join(case)) for case in permutations(numbers, i)])
    
    for case in cases:
        if is_prime_number(case): answer += 1
            
    return answer
