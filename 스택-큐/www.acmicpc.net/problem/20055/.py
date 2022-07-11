import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    BELT, ROBOT = deque(list(map(int, input().split()))), deque([0]*(N))
    EMPTY, GET = [0], 0

    for answer in range(1, N*max(BELT)*2+1):
        BELT.rotate(1)
        ROBOT.rotate(1)
        ROBOT[-1] = 0
        
        for i in range(N-2, -1, -1):
            if ROBOT[i] and not ROBOT[i+1] and BELT[i+1]:
                ROBOT[i], ROBOT[i+1] = ROBOT[i+1], ROBOT[i]
                BELT[i+1] -= 1
                EMPTY[GET] += (BELT[i+1] == 0)

        ROBOT[-1] = 0

        if not ROBOT[0] and BELT[0]:
            ROBOT[0] = 1
            BELT[0] -= 1
            EMPTY[GET] += (BELT[0] == 0)

        if EMPTY[GET] >= K:
            return answer

print(solution())
