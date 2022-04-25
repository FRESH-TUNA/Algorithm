import re
from collections import Counter

def solution(s):
    return [int(k) for k, v in Counter(re.findall('\d+', s)).most_common()]
