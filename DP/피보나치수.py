def solution(n):
    memory = [0, 1] + [0] * 100000
    for i in range(2, n+1):
        memory[i] = memory[i-1] + memory[i-2]
    return memory[n] % 1234567
