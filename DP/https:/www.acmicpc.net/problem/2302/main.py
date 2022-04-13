import sys, heapq

def init():
    input = sys.stdin.readline
    N, M = int(input()), int(input())
    VIP = set(int(input()) for _ in range(M))
    return N, M, VIP

def db():
    DB, DB[0], DB[1] = [0] * 41, 1, 1
    for i in range(2, 41):
        DB[i] = DB[i-1] + DB[i-2]
    return DB
    
def solution(N, M, VIP):
    DB, res = db(), 1

    sub_res = 0
    for i in range(1, N+1):
        if i in VIP: 
            res *= DB[sub_res]
            sub_res = 0
        else: sub_res += 1
    print(res*DB[sub_res])

if __name__ == '__main__':
    solution(*init())
