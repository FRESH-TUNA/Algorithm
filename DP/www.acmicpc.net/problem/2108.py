import sys
from collections import Counter

DB, N = [0] * 8001, 0
REAL_DB = None
START = 4000

def solution():
    calc_real_db()
    return avg(), mid(), preq(), rang()

def calc_real_db():
    REAL_DB_idx, DB_idx = 0, 0
    while REAL_DB_idx < N:
        for _ in range(DB[DB_idx]):
            REAL_DB[REAL_DB_idx] = DB_idx - START
            REAL_DB_idx += 1
        DB_idx += 1
    
def avg(): return round(sum(REAL_DB) / N)
def mid(): return REAL_DB[N // 2]
def preq(): 
    cs = Counter(REAL_DB).most_common()
    if len(cs) == 1 or cs[0][1] != cs[1][1]: return cs[0][0]
    return sorted(filter(lambda x: x[1] == cs[0][1], cs))[1][0]
def rang(): return REAL_DB[-1] - REAL_DB[0]

# driver
input = sys.stdin.readline
N = int(input())
REAL_DB = N * [0]
for _ in range(N): DB[int(input()) + 4000] += 1
print('\n'.join(map(str, solution())))
