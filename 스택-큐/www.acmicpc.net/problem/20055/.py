from collections import deque

def solution():
    N, K = map(int, input().split())
    robot, belt = deque([0]*N), deque(map(int, input().split()))
    empty = 0

    for answer in range(1, N*max(belt)*2+1):
        # 회전해라
        robot.rotate(1)
        belt.rotate(1)

        # 내려라
        robot[N-1] = 0
        for n in range(N-2, -1, -1):
            if robot[n] and not robot[n+1] and belt[n+1]:
                robot[n+1], robot[n] = 1, 0
                belt[n+1] -= 1
                empty += (belt[n+1] == 0)

        # 내려라
        robot[N-1] = 0
        if not robot[0] and belt[0]:
            robot[0] = 1
            belt[0] -= 1
            empty += (belt[0] == 0)

        if empty >= K: return answer
        
print(solution())
