def solution(n):
    result = []
    
    def hanoi(n, From, to, support):
        if n==0:
            return
        hanoi(n-1, From, support, to)
        result.append((From, to))
        hanoi(n-1, support, to, From)
    
    hanoi(n, 1, 3, 2)
    return result

