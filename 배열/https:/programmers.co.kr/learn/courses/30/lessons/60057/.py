def compress(s, l):
    root = [s[i:i+l] for i in range(0, len(s), l)]
    compared = root[1:] + [""]
    res, w = 0, 1

    for r, c in zip(root, compared):
        if r == c: w += 1
        else:
            res += (len(str(w)) if w > 1 else 0) + len(r)
            w = 1
    return res   

def solution(s):
    # 전체길이일때 압축
    answer = len(s)
    
    # 길이의 절반만큼 만검사
    for length in range(1, len(s)//2 + 1): 
        answer = min(answer, compress(s, length))
    return answer
