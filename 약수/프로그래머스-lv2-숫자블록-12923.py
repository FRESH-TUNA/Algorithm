def solution(begin, end):
    answer = []
    
    for n in range(begin, end+1):
        k = 0 if n==1 else 1

        for i in range(2, int(n**0.5) + 1):
            if n%i == 0 and n//i <= 10000000:
                k = n//i
                break
        answer.append(k)
    return answer
         
