import sys

def init():
    input = sys.stdin.readline
    return input().rstrip(), input().rstrip()

def solution(A, B):
    DB = [[0]*(len(B)+1) for _ in range(len(A)+1)]
    res = 0
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                DB[i][j] = 1 + DB[i-1][j-1]
                res = max(res, DB[i][j])
    print(res)

if __name__ == '__main__':
    solution(*init())
