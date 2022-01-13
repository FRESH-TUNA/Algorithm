def solution(board, moves):
    storages = [[]] + [list(reversed(list(filter(
        lambda x: x != 0, x)))) for x in zip(*board)] 
    answer, stack = 0, []
    
    for move in moves: 
        if not storages[move]: continue

        value = storages[move].pop()
        if not stack or stack[-1] != value: stack.append(value)
        else: 
            while stack and stack[-1] == value: 
                answer += (stack.pop() + 99) // 100
            answer += 1

    return answer
