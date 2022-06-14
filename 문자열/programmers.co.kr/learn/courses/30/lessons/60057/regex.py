import re

def solution(s):
    def compress(s, length):
        regex = re.compile(f'([a-z]{{{length}}})\\1*')
        last_match = None
        result = ""

        for match in regex.finditer(s):
            last_match = match
            start, end = match.span()
            i = (end-start) // length
            result += ([str(i), ""][i == 1] + length*"*")
        
        return (len(result) + len(s) - last_match.span()[1])

    if len(s) == 1: return 1
    return min(len(s), min(compress(s, l) for l in range(1, len(s)//2+1)))
