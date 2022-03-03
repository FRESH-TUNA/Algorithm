# https://www.acmicpc.net/problem/2240

from sys import stdin

def solution(T, W, jadus):
    db = [[[0 for _ in range(W+2)] for _ in range(T+1)] for _ in range(3)]
    ans = 0
    for i in range(1, T+1):
        for j in range(1, W+2):
            if jadus[i] == 1:
                db[1][i][j] = max(db[1][i-1][j] + 1, db[2][i-1][j-1] + 1)
                db[2][i][j] = max(db[1][i-1][j-1], db[2][i-1][j])
            else:
                if i == 1 and j == 1: continue
                db[1][i][j] = max(db[1][i-1][j], db[2][i-1][j-1])
                db[2][i][j] = max(db[1][i-1][j-1] + 1, db[2][i-1][j] + 1)

    for i in range(1, 3):
        for j in range(1, W+2):
            ans = max(ans, db[i][T][j])
    return ans

# driver
T, W = map(int, stdin.readline().split())
jadus = [0]
for _ in range(T): jadus.append(int(stdin.readline()))
print(solution(T, W, jadus))