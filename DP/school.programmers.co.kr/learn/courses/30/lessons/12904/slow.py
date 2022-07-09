def solution(s):
    N = len(s)
    answer = 0
    
    for i in range(N):
        for j in range(i+1, N+1):
            case = s[i:j]
            if case == case[::-1]:
                answer = max(answer, j-i)
    return answer
