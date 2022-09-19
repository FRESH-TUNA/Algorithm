from collections import defaultdict

def solution(surveys, choices):
    types = (('R','T'), ('C','F'), ('J','M'), ('A','N'))
    total_score = defaultdict(lambda: 0)
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    result = []

    for survey, choice in zip(surveys, choices):
        if choice > 4:
            total_score[survey[1]] += score[choice]
        if choice < 4:
            total_score[survey[0]] += score[choice]

    for type1, type2 in types:
        score1, score2 = total_score[type1], total_score[type2]
        result.append([type2, type1][score1>=score2])
    return ''.join(result)
