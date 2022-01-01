from collections import Counter

def solution(s):
    iterated, zeros = 0, 0
    while len(s) > 1:
        counter = Counter(s)
        zeros, iterated = zeros + counter["0"], iterated + 1
        s = bin(counter["1"])[2:]
    return [iterated, zeros]
