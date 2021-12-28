def solution(s):
    for i in range(len(s)):
        result = check(s[i:] + s[:i])
        if result: return result 
    return 0

def check(s):
    check = {"[": "]", "(": ")", "{": "}"}
    answer, stack = 0, []
    for c in s:
        if c in ("[", "(", "{"): stack.append(c)
        elif len(stack) == 0 or check[stack[-1]] != c:
            return 0
        else: 
            stack.pop()
            answer += (len(stack) == 0)
    return 0 if len(stack) else answer

#######

