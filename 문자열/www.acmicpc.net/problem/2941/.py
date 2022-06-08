import re, sys

def solution(s):
    print(len(re.findall("(c=|c-|dz=|d-|lj|nj|s=|z=|\w)", s)))

solution(sys.stdin.readline().rstrip())
