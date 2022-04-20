import sys

def init():
    input = sys.stdin.readline
    return input(), input()

def solution(A, B):
    long, short = None, None

    if len(A) >= len(B):
        long, short = A, B
    else:
        short, long = A, B

    left, res = 0, 0
    for right in range(1, len(short)):
        while left+1 != right:
            if find(short[left:right], long): 
                res = max(res, right-left)
                break
            else: left += 1
    print(res)

def find(word, long):
    N = len(word)
    for i in range(len(long)-N):
        if word == long[i:i+N]: return True
    return False

if __name__ == '__main__':
    solution(*init())
