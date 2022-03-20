import re
from collections import Counter

def solution(s):
    return [int(value) for value, _ in Counter(re.findall("\d+", s)).most_common()]
