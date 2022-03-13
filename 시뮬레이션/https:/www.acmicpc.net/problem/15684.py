import sys

# global static
N, H = 0, 0

def solution(db):
    for max_cnt in range(4):
        if dfs(db, 1, 1, 0, max_cnt): 
            return max_cnt
    return -1

def dfs(db, x, y, cnt, max_cnt):
    if check(db): return True
    if cnt == max_cnt: return False

    # 가로선
    for i in range(x, H+1):
        # 가로선이 같으면 주어진 세로선 부터 탐색
        for j in range(y if i == x else 1, N):
            if db[i][j]: j += 1
            else:
                db[i][j] = 1
                # 세로선을 이어서 붙이지 못해서 +2 한다
                if dfs(db, i, j+2, cnt+1, max_cnt):
                    return True
                db[i][j] = 0
    return False
        

# 모든 세로선에 대해 자신의 세로선으로 돌아가는지 check 한다
def check(db):
    for start in range(1, N+1):
        i = start
        for h in range(1, H+1):
            if db[h][i]: i += 1
            elif i-1 and db[h][i-1]: i -= 1
        if i != start: return False
    return True

# driver
input = sys.stdin.readline
N, M, H = map(int, input().split())
# 각 가로선당 세로선
db = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    # 가로선 / 세로선
    x, y = map(int, input().split())
    db[x][y] = 1
