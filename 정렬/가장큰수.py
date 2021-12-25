def solution(numbers):
    return str(int(''.join(sorted([str(num) for num in numbers], key=lambda x: x*3, reverse=True))))
