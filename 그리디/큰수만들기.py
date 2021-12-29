def solution(number, k):
    number, stack = [int(n) for n in number], []

    for idx, n in enumerate(number):
        if not stack or stack[-1] > n: stack.append(n)
        else:
            while stack and stack[-1] < n and k > 0: 
                stack.pop()
                k -= 1
            stack.append(n)
        if k == 0: return "".join(map(str, stack + number[idx + 1:]))
    
    return "".join(map(str, stack[:k * (-1)]))
