import sys
from collections import defaultdict

def init():
    input = sys.stdin.readline
    N, K = int(input()), int(input())
    return N, K

def solution(N, K):
    start, end = 1, K*K
    while start <= end:
        mid = start + (end - start) // 2
        count = 0
        for i in range(1, N+1): count += min(mid//i, N)  
        if count >= K: end = mid-1
        else: start = mid+1
    print(start)
    

if __name__ == '__main__':
    solution(*init())