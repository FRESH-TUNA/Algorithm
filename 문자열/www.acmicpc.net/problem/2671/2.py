import re, sys

def solution(s):
    print("SUBMARINE" if re.match("(100+1+|01)+$", s) != None else "NOISE")

solution(sys.stdin.readline().rstrip())
