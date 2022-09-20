from itertools import combinations_with_replacement

def solution(n, apeach_result):
    MAX_SCORE = 11
    cur_difference, last_cur_difference, GET = [-1], [-1], 0
    lions_result = [0]*MAX_SCORE
    answer = [0]*MAX_SCORE
    apeach_result = list(reversed(apeach_result))
    
    def can_answer():
        lion, apeach = 0, 0
        
        for score in range(MAX_SCORE):
            if apeach_result[score]==0 and lions_result[score]==0:
                continue
            if apeach_result[score] >= lions_result[score]:
                apeach += score
            else:
                lion += score
        last_cur_difference[GET] = lion-apeach
        return last_cur_difference[GET] > cur_difference[GET]
    
    def update_answer():
        for i in range(MAX_SCORE):
            answer[i] = lions_result[i]
        cur_difference[GET] = last_cur_difference[GET]

    def call():
        for case in combinations_with_replacement(range(MAX_SCORE), n):
            for c in case:
                lions_result[c] += 1
            
            if can_answer():
                update_answer()

            for i in range(MAX_SCORE):
                lions_result[i] = 0
        return [-1] if cur_difference[GET]<=0 else list(reversed(answer))
    
    return call()

