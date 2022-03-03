# https://www.acmicpc.net/problem/2193

from sys import stdin

def solution(n):
    db, db[1] = [[0, 0] for _ in range(n+1)], [0, 1]
    for i in range(2, n+1):
        db[i][0], db[i][1] = sum(db[i-1]), db[i-1][0]
    return sum(db[-1])
# driver
print(solution(int(stdin.readline())))
