def solution(b, moves):
    crain = [[]] + [[x for x in reversed(s) if x] for s in zip(*b)]
    ans, stack = 0, []
    for move in moves:
        if not len(crain[move]): continue
        data = crain[move].pop()
        if len(stack) and stack[-1] == data: ans += pop(stack, data)
        else: stack.append(data)        
    return ans
    
def pop(stack, data, ans=1):
    while len(stack) and stack[-1] == data:
        ans += stack.pop() // 101 + 1
    return ans
