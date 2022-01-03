# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for char in s:
        if len(stack) == 0 or stack[-1] != char: stack.append(char)
        elif stack[-1] == char: stack.pop()
    return 1 if len(stack) == 0 else 0
