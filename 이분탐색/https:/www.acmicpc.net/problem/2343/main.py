import sys

def init():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    VIDEOS = list(map(int, input().split()[:N]))
    return N, M, VIDEOS

def solution(N, M, VIDEOS):
    left, right, res = 1, 1000000000, 1000000000

    while left <= right:
        max_size = left + (right-left) // 2
        cur_size, cur_disks = 0, 1
        for v in VIDEOS:
            if v > max_size:
                cur_disks = 0
                break
            if v + cur_size > max_size:
                cur_disks += 1
                cur_size = v
            else: cur_size += v

        if cur_disks and cur_disks <= M:
            res = max_size
            right = max_size-1
        else: left = max_size+1
    print(res)

if __name__ == '__main__':
    solution(*init())
