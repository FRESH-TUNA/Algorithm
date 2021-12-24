# https://programmers.co.kr/learn/courses/30/lessons/60058

# 첫번째 풀이
def solution(p):
    return make_correct_string(p)

def seperate(p):
    left, right = 0, 0
    for index, char in enumerate(p):
        if char == "(": left += 1
        else: right += 1
        if left == right: return (p[:index + 1], p[index + 1:])
    return -1
    
def correct(p):
    stacked = 0
    for char in p:
        if char == "(": stacked += 1
        elif stacked == 0: return False
        else: stacked -= 1
    return stacked == 0
    
def reverse(p):
    return "".join(["(" if char == ")" else ")" for char in p])

def make_correct_string(p):
    # 입력이 빈문자열 빈문자열 반환
    if p == "": return p
    
    # "균형잡힌 괄호 문자열" u, v로 분리
    u, v = seperate(p)
    if correct(u): return u + make_correct_string(v)
    else: return "(" + make_correct_string(v) + ")" + reverse(u[1:-1])
