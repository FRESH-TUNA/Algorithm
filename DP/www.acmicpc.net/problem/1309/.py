import sys

input = sys.stdin.readline
N = int(input())
db = [[0, 0, 0] for _ in range(N)]

def solution():
    db[0][0], db[0][1], db[0][2] = 1, 1, 1
    for i in range(1, N):
        db[i][0] = (db[i-1][1] + db[i-1][2]) % 9901
        db[i][1] = (db[i-1][0] + db[i-1][2]) % 9901
        db[i][2] = (db[i-1][0] + db[i-1][1] + db[i-1][2]) % 9901
    print(sum(db[-1]) % 9901)

solution()
