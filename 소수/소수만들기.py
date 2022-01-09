import math
from itertools import combinations

def solution(nums):
    MAX_CHAE, step = 3000, 1 
    chae, max_step = [True] * MAX_CHAE, int(math.sqrt(MAX_CHAE))
    cases = [sum(c) for c in combinations(nums, 3)]

    while step < max_step:
        step += 1
        if not chae[step]: continue
        for n in range(step * 2, MAX_CHAE, step): chae[n] = False
    
    return len(list(filter(lambda x: chae[x], cases)))
