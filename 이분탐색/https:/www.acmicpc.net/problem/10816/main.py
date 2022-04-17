import sys

def init():
    input = sys.stdin.readline
    N = int(input())
    CARDS = sorted(map(int, input().split()[:N]))
    M = int(input())
    FINDS = list(map(int, input().split()[:M]))
    return N, CARDS, M, FINDS

def solution(N, CARDS, M, FINDS):
    print(' '.join(str(count(N, CARDS, f)) for f in FINDS))

def count(N, CARDS, find):
    # lower bound
    left, right, upper = 0, N-1, -1 
    while(left <= right):
        mid = left + (right-left) // 2
        if CARDS[mid] <= find: 
            left, upper = mid+1, mid
        else: right = mid-1
    
    # upper bound
    left, right, under = 0, N-1, N 
    while(left <= right):
        mid = left + (right-left) // 2
        if CARDS[mid] >= find: right, under = mid-1, mid
        else: left = mid+1

    if upper == -1 or under == N: return 0
    else: return (upper - under + 1) if upper >= under else 0
    
if __name__ == '__main__':
    solution(*init())
