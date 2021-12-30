import math

def solution(n, words):
    db, failed = {words[0]}, [n] + [i for i in range(1, n)]
    for i, (l_word, word) in enumerate(zip(words, words[1:])):
        if word in db or l_word[-1] != word[0]: 
            return [failed[(i + 2) % n], math.ceil((i + 2) / n)]
        else: db.add(word)
    return [0, 0]
