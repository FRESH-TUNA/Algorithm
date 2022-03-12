import sys
from collections import deque

# global static
RIGHT, LEFT = 1, -1
NORTH, EAST, WEST = 0, 2, 6
N = 4

def solution(wheels, COMMANDS):
    CHECKS = ((), ((2, 1), (3, 2), (4, 3)), ((1, 2), (3, 2), (4, 3)),
              ((2, 3), (4, 3), (1, 2)), ((3, 4), (2, 3), (1, 2)))

    for (i, d) in COMMANDS:
        turn_wheels(wheels, get_turns(wheels, CHECKS[i], i, d))
    return score(wheels)

def get_turns(wheels, cases, i, d):
    NEW_D = [0, LEFT, RIGHT]
    res, res[i] = [0] * (N+1), d

    for (t_i, s_i) in cases:
        target, source = wheels[t_i], wheels[s_i]
        if res[s_i] == 0: 
            continue
        elif t_i > s_i and source[EAST] != target[WEST]: 
            res[t_i] = NEW_D[res[s_i]]
        elif t_i < s_i and source[WEST] != target[EAST]: 
            res[t_i] = NEW_D[res[s_i]]          
    return res

def turn_wheels(wheels, turns):
    for i in range(1, N+1): turn_wheel(wheels[i], turns[i])

def turn_wheel(wheel, d): 
    if d == RIGHT: wheel.appendleft(wheel.pop())
    elif d == LEFT: wheel.append(wheel.popleft())

def score(wheels):
    SCORES = ((), (0, 1), (0, 2), (0, 4), (0, 8))
    return sum(SCORES[w][wheels[w][NORTH]] for w in range(1, N+1))
    
# driver
wheels = [None] + [deque(map(int, list(input()))) for _ in range(N)]
COMMANDS_N = int(input())
COMMANDS = [list(map(int, input().split()[:2])) 
            for _ in range(COMMANDS_N)]
print(solution(wheels, COMMANDS))
