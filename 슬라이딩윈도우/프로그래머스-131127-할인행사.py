from collections import Counter

def solution(want, number, discount):
    WANT, CURRENT = Counter(), Counter()
    N = 10
    
    for w, n in zip(want, number):    
        WANT[w] = n
        
    for n in range(N):
        CURRENT[discount[n]] += 1
        
    answer = 1 if (WANT&CURRENT)==WANT else 0

    for n in range(len(discount)-N):
        CURRENT[discount[n]] -=1
        CURRENT[discount[n+N]] += 1
        
        if (WANT&CURRENT)==WANT:
            answer += 1

    return answer
