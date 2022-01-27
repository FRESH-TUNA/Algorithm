def solution(a, b, g, s, w, t):
    start, end = 0, (10**9*2) * (10**5*2)
    ans, cities = end, list(zip(g, s, w, t))
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0
        
        for (_gold, _silver, _weight, _time) in cities:
            moves = mid // (_time * 2)
            if mid % (_time * 2) >= _time: moves += 1
                
            gold += min(_gold, moves * _weight)
            silver += min(_silver, moves * _weight)
            total += min(_gold + _silver, moves * _weight)
        
        if gold >= a and silver >= b and total >= a+b:
            answer, end = mid, mid-1
        else: start = mid+1

    return answer
