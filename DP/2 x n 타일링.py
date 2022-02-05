def solution(n):
    db = [0, 1, 2]
    for x in range(3, n+1): 
        db.append((db[-1] + db[-2]) % 1000000007)
    return db[-1]