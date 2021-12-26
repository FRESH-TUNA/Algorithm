# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
from functools import reduce
import math

def is_prime(num):
    if num in (0, 1): return False
    for case in range(2, int(math.sqrt(num)) + 1):
        if num % case == 0: return False
    return True

def solution(numbers):
    cases = set()
    for i in range(1, len(numbers) + 1):
        cases |= {int(''.join(case)) for case in permutations(numbers, i)}
    return reduce(
        lambda acc, case: acc + (1 if is_prime(case) else 0), cases, 0)
