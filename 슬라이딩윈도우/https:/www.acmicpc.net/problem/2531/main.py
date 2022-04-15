import sys
from collections import defaultdict

def init():
    input = sys.stdin.readline
    N, D, K, C = map(int, input().split())
    RICES = [int(input()) for _ in range(N)] * 2
    return N, D, K, C, RICES

def solution(N, D, K, C, RICES):
    db = defaultdict(lambda: 0)
    for x in RICES[:K]: db[x] += 1
    res = len(db) + (C not in db)

    for i in range(N-1):
        l, r = i, i+K
        db[RICES[r]] += 1
        db[RICES[l]] -= 1
        if not db[RICES[l]]: del db[RICES[l]]
        res = max(res, len(db) + (C not in db))
    print(res)

if __name__ == '__main__':
    solution(*init())
