# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re
from collections import deque 

def calc(expression, priorities):
    tokens = deque(re.split('([-*+])', expression))
    
    for p in priorities:
        next_tokens = deque()
        while tokens:
            token = tokens.popleft()
            next_tokens.append(token if token != p else str(eval(next_tokens.pop() + token + tokens.popleft())))
        tokens = next_tokens
        
    return abs(int(tokens[0]))
           
def solution(expression):
    return max([calc(expression, p) for p in permutations(("*", "+", "-"), 3)])
