import math

def solution(n, k):
    MAX_N, FACTORIALS = 20, [0]*20
    CASES = [i+1 for i in range(n)]
    answer = []
    
    def factorialInit():
        FACTORIALS[1] = 1
        for i in range(2, MAX_N):
            FACTORIALS[i] = FACTORIALS[i-1]*i
        
    def call():
        _k = k
        for i in range(n-1):
            baseValue = FACTORIALS[n-i-1]
            divided, remain = (_k)//baseValue, (_k)%baseValue

            if remain != 0:
                divided += 1
            
            answer.append(CASES[divided-1])
            del CASES[divided-1]
            _k = remain
        
        answer.append(CASES[0])
        return answer
    
    factorialInit()
    return call()

