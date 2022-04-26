import sys

# global
N, M = 0, 0
STRING, PATTERN = '', ''
LPS = []

def init():
    global STRING, PATTERN, LPS, N, M
    input = sys.stdin.readline
    STRING, PATTERN = input().rstrip(), input().rstrip()
    N, M = len(STRING), len(PATTERN)
    LPS = [0]*M

def preprocessing():
    same_leng = 0
    i = 1
    
    while i < M:
        if PATTERN[i] == PATTERN[same_leng]:
            same_leng += 1
            LPS[i] = same_leng
            i += 1
        elif same_leng != 0:
            same_leng = LPS[same_leng-1]
        else:
            LPS[i] = 0
            i += 1

def solution():
    i = j = res = 0
    
    while i < N:
        if PATTERN[j] == STRING[i]:
            i, j = i+1, j+1
        elif j != 0:
            j = LPS[j-1]
        else:
            i += 1
    
        if j == M:
            j, res = LPS[j-1], res+1
    print(1 if res > 0 else 0)

init()
preprocessing()
solution()
