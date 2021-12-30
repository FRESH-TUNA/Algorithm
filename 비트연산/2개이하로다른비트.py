def fx(num):
    if num & 1:
        num = ["0"] + [d for d in bin(num)[2:]]
        for i in range(len(num) - 2, -1, -1):
            if num[i] == "0":
                num[i], num[i + 1] = "1", "0"
                return int("".join(num), 2)
    return num + 1
    
def solution(numbers):
    return [fx(n) for n in numbers]
