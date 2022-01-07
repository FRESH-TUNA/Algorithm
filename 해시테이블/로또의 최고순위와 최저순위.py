def solution(lottos, win_nums):
    num_of_zeros, mini, result = 0, 0, [6] + list(range(6, 0, -1))
    db = set(str(x) for x in win_nums)
    for x in lottos:
        if x == 0: num_of_zeros += 1
        elif str(x) in db: mini += 1    
    return [result[num_of_zeros + mini], result[mini]]
