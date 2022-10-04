def solution(quiz, answer=[]):
    for A, op, B, _, res in [q.split() for q in quiz]:
        answer.append(["X", "O"][int(A)+int(B)*[1,-1][op=='-']==int(res)])
    return answer

