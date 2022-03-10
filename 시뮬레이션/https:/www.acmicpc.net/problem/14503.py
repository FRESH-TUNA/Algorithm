import sys

def solution(N, M, x, y, d, traced):
    ans = 0
    MOVE_X, MOVE_Y = (-1, 0, 1, 0), (0, 1, 0, -1)
    LEFT, CLEANED, BORDER = (3, 0, 1, 2), 2, 1
    MOVE_N = 4

    while True:
        if not traced[x][y]:
            traced[x][y] = CLEANED
            ans += 1

        is_move = False
        for _ in range(MOVE_N):
            d = LEFT[d]
            nx, ny = MOVE_X[d]+x, MOVE_Y[d]+y
            if not in_border(N, M, nx, ny) or traced[nx][ny]: 
                continue
            else:
                is_move = True
                x, y = nx, ny
                break
        if is_move: continue

        nx, ny = x-MOVE_X[d], y-MOVE_Y[d]
        if not in_border(N, M, nx, ny): return ans
        if traced[nx][ny] == BORDER: return ans
        x, y = nx, ny
    return ans


def in_border(N, M, x, y):
    return not (x in (-1, N) or y in (-1, M))

# driver
input = sys.stdin.readline
N, M = map(int, input().split())
x, y, d = map(int, input().split())
traced = [ list(map(int, input().split()[:M])) 
          for _ in range(N) ]
print(solution(N, M, x, y, d, traced))
