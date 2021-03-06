import re

def solution(s):
    def compress(s, length):
        REGEX = re.compile(f'([a-z]{{{length}}})\\1*')
        answer = 0
        
        for match in re.finditer(REGEX, s):
            start, end = match.span()
            count = (end-start) // length    
            answer += [len(str(count)) , 0][count == 1] + length
        return answer + len(s) % length

    return min(compress(s, i) for i in range(1, len(s) // 2 + 2))
