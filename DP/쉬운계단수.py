from sys import stdin

def solution(n):
    db = [[0 for _ in range(10)] for _ in range(n+1)]
    db[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n+1):
        for j in range(10):
            if j > 0: db[i][j] += db[i-1][j-1]
            if j < 9: db[i][j] += db[i-1][j+1]
            db[i][j] = db[i][j] % 1000000000
            
    return sum(db[-1]) % 1000000000

# driver
print(solution(int(stdin.readline())))
