import re

def solution(s):
    print(re.split("\d+", s))
    print(len(re.split("\d+", s)))
    return len(re.split("^[\d+]", s)) == 1 and len(s) in (4, 6)
