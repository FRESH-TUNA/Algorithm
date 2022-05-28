import sys
sys.setrecursionlimit(10 ** 5)

# global
input = sys.stdin.readline
N, W = int(input()), int(input())
Dests = [list(map(int, input().split())) for _ in range(W)]
DB = [[-1 for _ in range(W+1)] for _ in range(W+1)]
PolicesDB = []

def distance(police, target, start):
    police_x, police_y, target_x, target_y = 0, 0, 0, 0
    target_x, target_y = Dests[target-1]
    
    if start == 1:
        police_x, police_y = 1, 1
    elif start == 2:
        police_x, police_y = N, N
    else:
        police_x, police_y = Dests[police-1]
 
    return abs(police_x-target_x) + abs(police_y-target_y)

def dfs(car1, car2):
    if car1 == W or car2 == W:
        return 0
    if DB[car1][car2] != -1:
        return DB[car1][car2]
    target = max(car1, car2)

    car1_res = dfs(target, car2) + distance(car1, target, [0, 1][car1==0])
    car2_res = dfs(car1, target) + distance(car2, target, [0, 2][car2==0])

    DB[car1][car2] = min(tmp1,tmp2);
    PolicesDB[car1][car2] = [2, 1][car1_res < car2_res]
    return DB[car1][car2]

# drivers
print(dfs(0, 0))
