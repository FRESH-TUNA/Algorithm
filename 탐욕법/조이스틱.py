# https://programmers.co.kr/learn/courses/30/lessons/42860
# https://bellog.tistory.com/152

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next_pos = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 연속되는 구간
        next_pos = i + 1
        while next_pos < len(name) and name[next_pos] == 'A':
            next_pos += 1
        
        # 되돌아갈때랑 비교해서 판단
        min_move = min(min_move, i + i + len(name) - next_pos)
    answer += min_move
    return answer
