def solution(left, right, counts=[]):
    for x in range(left, right + 1): counts.append(count(x))
    counts = zip(range(left, right + 1), counts)
    return sum(v * (-1) if c & 1 else v for v, c in counts)
  
def count(x, answer=0):
    for i in range(1, x // 2 + 1): 
        if x % i == 0: answer += 1
    return answer + 1
    