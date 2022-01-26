def solution(a, b, g, s, w, t):
    start, end = 0, (10**9) * 2 * (10**5) * 2    
    cities, answer = list(zip(g, s, w, t)), end

    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0
        
        for city in cities:
            _gold, _silver, _weight, _time = city
            
            # 시간동안 도시에서 자원을 가지고 올수 있는 횟수
            moves = mid // (_time * 2)
            if mid % (_time * 2) >= _time: moves += 1
            # 최대 골드/실버/(골드, 실버)
            gold += _gold if (_gold < moves * _weight
                             ) else (moves * _weight)
            silver += _silver if (_silver < moves * _weight
                                 ) else (moves * _weight)
            total += _gold + _silver if(
                _gold + _silver < moves * _weight
            ) else moves * _weight

        if gold >= a and silver >= b and total >= a+b:
            end, answer = mid - 1, min(answer, mid)
        else: start = mid + 1
    return answer