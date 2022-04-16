import sys
from collections import defaultdict

def init():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    HOUSES = sorted(int(input()) for _ in range(N))
    return N, C, HOUSES

def solution(N, C, HOUSES):
    start, end = 1, HOUSES[-1]-HOUSES[0]
    answer = 0
    while start <= end:
        
        mid = start + (end - start) // 2
        cur, cnt = HOUSES[0], 1

        for i in range(1, len(HOUSES)):
            if HOUSES[i] >= cur + mid:
                cnt += 1
                cur = HOUSES[i]
        if cnt >= C:
            start = mid + 1
            answer = mid
        else: end = mid-1
    print(answer)

if __name__ == '__main__':
    solution(*init())
