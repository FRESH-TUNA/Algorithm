import sys

def solution(T, consults):
    db = [0] * (T+1)
    for i in range(T):
        t, v = consults[i]

        # i번째날에서 일을 하고 보상을 받은 경우
        if i+t <= T:
            db[i+t] = max(db[i+t], db[i] + v)

        # i번째 날에서 일을 안한다면
        db[i+1] = max(db[i+1], db[i])

    return max(db)

# driver
input = sys.stdin.readline
T = int(input())
consults = [list(map(int, input().split()[:2])) for _ in range(T)]
print(solution(T, consults))
