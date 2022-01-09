from collections import OrderedDict

def solution(answers):
    answer, results = OrderedDict(), [1, 2, 3]
    fools = [(1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4, 2, 5), 
             (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)]
    counts = [(len([a for i, a in enumerate(answers) 
            if f[i % len(f)] == a]), i+1) for i, f in enumerate(fools)]
    
    for key, c in sorted(counts, reverse=True): 
        if str(key) in answer: answer[str(key)].append(c)
        else: answer[str(key)] = [c]
    
    answer = answer.popitem(last=False)
    return sorted(answer[1]) if answer[0] != 0 else []
