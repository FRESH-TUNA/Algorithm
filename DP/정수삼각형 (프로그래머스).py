# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    db = [[0, 0], [0, triangle[0][0], 0]]
    t = [[0, 0]] + [[0] + row + [0] for row in triangle]
    
    # answer[i][j] = max(answer[i-1][j], answer[i-1][j-1])
    for i in range(2, len(t)):
        _db = [0]
        for j in range(1, len(t[i]) - 1):
            _db.append(max(db[i-1][j], db[i-1][j-1]) + t[i][j])
        db.append(_db + [0])
    
    return max(db[-1])
