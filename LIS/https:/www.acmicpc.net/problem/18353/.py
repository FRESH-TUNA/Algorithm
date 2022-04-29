import sys
import bisect

# global
N = None
DATA = None

def init():
    global N, DATA
    input = sys.stdin.readline
    N = int(input())
    DATA = reversed(list(map(int, input().rstrip().split())))

def solution():
    result = []
    
    for d in DATA:
        idx = bisect.bisect_left(result, d)
        if idx >= len(result): result.append(d)
        else: result[idx] = d
    print(N-len(result))

init()
solution()
