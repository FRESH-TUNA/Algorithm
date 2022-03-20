# https://programmers.co.kr/learn/courses/30/lessons/60057

def compress(s, length):
    result = ''

    # 조각을 낸 리스트
    tokens = [ s[i:i + length] for i in range(0, len(s), length) ]
    
    # 리스트를 검사하여 결과 도출
    comparator, comparator_count = tokens[0], 1
    for token in tokens[1:]:
        if comparator == token: comparator_count += 1
        else: 
            result = result + (str(comparator_count) if comparator_count > 1 else '') + comparator
            comparator, comparator_count = token, 1
            
    # 처리안 된 comparator 처리
    if comparator_count > 0:
        result = result + (str(comparator_count) if comparator_count > 1 else '') + comparator
    
    return result
        
    
def solution(s):
    # 전체길이일때 압축
    answer = len(s)
    
    # 길이의 절반만큼 만검사
    for length in range(1, len(s) // 2 + 1): answer = min( answer, len(compress(s, length)) )
    return answer