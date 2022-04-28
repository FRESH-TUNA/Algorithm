import sys

# global
DATA = ""
STRING = ""
LPS = []

def init():
    global DATA, STRING, LPS
    input = sys.stdin.readline
    STRING = input().rstrip()
    DATA = input().rstrip()
    LPS = [0] * len(DATA)

def lps():
    length = 0
    for i in range(1, len(DATA)):
        while length and DATA[length] != DATA[i]:
            length = LPS[length-1]
        if DATA[i] == DATA[length]: LPS[i] = LPS[i-1] + 1

def find():
    i = j = res = 0

    while i < len(STRING):
        if DATA[j] == STRING[i]:
            i += 1
            j += 1
        elif j != 0:
            j = LPS[j-1]
        else:
            i += 1

        # Pattern을 찾은 경우
        if j == len(DATA):
            res += 1
            j = LPS[j-1]
    print(res)

init()
lps()
find()