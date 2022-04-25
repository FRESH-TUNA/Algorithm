import re

def solution(s):
    return re.search("[^\d]", s) == None and len(s) in set((4, 6))
