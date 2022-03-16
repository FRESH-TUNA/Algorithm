import sys

def solution(x, y, w, h): return(min(w-x, x, h-y, y))

# driver
input = sys.stdin.readline
print(solution(*map(int, input().rstrip().split())))
