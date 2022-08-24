import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# main
N, W = int(input()), int(input())
events = [(1,1),(N,N)]
for _ in range(W):
    events.append(tuple(map(int,input().split())))
DB = [[-1 for _ in range(W+2)] for _ in range(W+2)]

def solution(car1, car2):
    if car1 == W+1 or car2 == W+1: return 0
    if DB[car1][car2] != -1: return DB[car1][car2]
    
    target = max(car1, car2) + 1
    car1_v = solution(target, car2) + abs(events[target][0]-events[car1][0]) + abs(events[target][1]-events[car1][1])
    car2_v = solution(car1, target) + abs(events[target][0]-events[car2][0]) + abs(events[target][1]-events[car2][1])
    DB[car1][car2] = min(car1_v, car2_v)
    return DB[car1][car2]

def trace(car1, car2):
    if car1 == W+1 or car2 == W+1: return
    target = max(car1, car2) + 1
    car1_v = abs(events[target][0]-events[car1][0]) + abs(events[target][1]-events[car1][1])
    car2_v = abs(events[target][0]-events[car2][0]) + abs(events[target][1]-events[car2][1])

    if DB[target][car2]+car1_v < DB[car1][target]+car2_v:
        print(1)
        trace(target, car2)
    else:
        print(2)
        trace(car1, target)

# result
print(solution(0, 1))
trace(0, 1)
