import sys

def solution(N, M, graph, ds, x, y):
    dice = [0, 0, 0, 0, 0, 0, 0]
    ans = []
    nxys = ((), (0, 1), (0, -1), (-1, 0), (1, 0))
    
    for d in ds:
        nx, ny = nxys[d][0]+x, nxys[d][1]+y
        if nx in (-1, N) or ny in (-1, M): continue

        rotate(dice, d)
        ans.append(str(dice[1]))
        
        if not graph[nx][ny]: graph[nx][ny] = dice[6]
        else:
            dice[6] = graph[nx][ny]
            graph[nx][ny] = 0

        x, y = nx, ny

    return '\n'.join(ans)

def rotate(d, direction):
    if direction == 1:
        d[1], d[3], d[6], d[4] = d[4], d[1], d[3], d[6]
    elif direction == 2:
        d[1], d[3], d[6], d[4] = d[3], d[6], d[4], d[1]
    elif direction == 3:
        d[1], d[5], d[6], d[2] = d[5], d[6], d[2], d[1]
    else:
        d[1], d[5], d[6], d[2] = d[2], d[1], d[5], d[6]

# driver
input = sys.stdin.readline
N, M, x, y, COMMANDS_N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ds = list(map(int, input().split()[:COMMANDS_N]))
print(solution(N, M, graph, ds, x, y))
