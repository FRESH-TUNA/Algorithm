import re, sys

def solution(s):
    finds = re.findall("(c=|c-|dz=|d-|lj|nj|s=|z=)", s)
    print(len(s) - sum(len(x) for x in finds) + len(finds))

solution(sys.stdin.readline().rstrip())
