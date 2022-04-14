import sys, heapq

def init():
    input = sys.stdin.readline
    N = int(input())
    nums = sorted(map(int, input().split()[:N]))
    return N, nums

def solution(N, nums):
    target = 1
    for n in nums:
        if target<n: break
        target += n
    print(target)

if __name__ == '__main__':
    solution(*init())
