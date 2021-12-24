# https://programmers.co.kr/learn/courses/30/lessons/17677

import collections
from functools import reduce

def make_tokens(s):
    shifted_str = s[1:] if len(s) else ""
    return [s[i] + shifted_str[i] for i in range(len(shifted_str)) if s[i].isalpha() and shifted_str[i].isalpha()]

def jakad(l1, l2):
    if len(l1) == 0 and len(l2) == 0: return 1
    l1, l2 = collections.Counter(l1), collections.Counter(l2)
    inter, union = list((l1 & l2).elements()), list((l1 | l2).elements())
    return len(inter) / len(union)

def solution(str1, str2):
    # 집합연산으로 자카드 유사도 측정
    return int(jakad(make_tokens(str1.upper()), make_tokens(str2.upper())) * 65536)


##
import math
from collections import Counter

def make_set(line):
    _set = list()
    for i in range(len(line) - 1):
        candidate = line[i:i + 2]
        if candidate.isalpha(): _set.append(candidate)
    return _set

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    set1, set2 = list(map(make_set, [str1, str2]))
    intersection = list((Counter(set1) & Counter(set2)).elements())
    union = list((Counter(set1) | Counter(set2)).elements())
    return 65536 if len(union) == 0 else math.trunc(len(intersection) \
        / len(union) * 65536)
