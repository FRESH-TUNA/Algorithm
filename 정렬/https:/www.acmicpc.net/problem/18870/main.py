import sys

# global
input = sys.stdin.readline
N, NUMS, MAP = 0, [], dict()

def solution():
    idx = 0
    for v in sorted(NUMS):
        if v in MAP: continue
        MAP[v] = idx
        idx += 1
    print(" ".join(str(MAP[n]) for n in NUMS))

# driver
N = int(input())
NUMS = list(map(int, input().split()[:N]))
solution()
