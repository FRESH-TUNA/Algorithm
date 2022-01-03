# https://programmers.co.kr/learn/courses/30/lessons/84512/solution_groups?language=python3


def solution(word):
    db, stack, answer, word = set(), ["A"], 1, list(word)
    
    while stack != word:
        _word = "".join(stack)

        if _word in db: 
            pop_or_shift(stack)
            continue
        
        db.add(_word)
        answer += 1
        
        if len(stack) == 5: pop_or_shift(stack)
        else: stack.append("A")
    return answer

def pop_or_shift(stack):
    next_char = {"A":"E", "E":"I", "I":"O", "O":"U"}
    if stack[-1] == "U": stack.pop()
    else: stack[-1] = next_char[stack[-1]]
