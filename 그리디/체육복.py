def solution(n, lost, reserve):
    answer, lost, reserve = n, set(lost), set(reserve)
    lost, reserve = lost - reserve, reserve - lost
    for x in range(1, n+1):
        if x not in lost: continue
        if x-1 in reserve: reserve.remove(x-1)
        elif x+1 in reserve: reserve.remove(x+1)
        else: answer -= 1
    return answer
