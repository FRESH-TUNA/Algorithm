from collections import Counter
import sys

def solution(n):
    _n = Counter(bin(n))
    for x in range(n+1, sys.maxsize):
        if Counter(bin(x))["1"] == _n["1"]: return x
