def compress(s, length):
    res = ''
    root, root_n, start = s[0:length], 0, 0

    while True:
        cur = s[start:start+length]
        if root == cur:
            root_n += 1
            start += length
        elif len(cur) < length:
            res += (str(root_n) if root_n > 1 else '') + root + cur
            break
        else:
            res += (str(root_n) if root_n > 1 else '') + root
            root, root_n = s[start:start+length], 0
    return len(res)

def solution(s):
    # 전체길이일때 압축
    answer = len(s)
    
    # 길이의 절반만큼 만검사
    for length in range(1, len(s)//2 + 1): 
        answer = min(answer, compress(s, length))
    return answer