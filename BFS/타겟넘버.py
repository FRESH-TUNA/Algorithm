# https://programmers.co.kr/learn/courses/30/lessons/43165

from functools import reduce

#BFS 풀이
def solution(numbers, target):
    leaves = [0]

    for number in numbers:
        next_leaves = []
        for parent in leaves:
            next_leaves += [parent + number, parent - number]
        leaves = next_leaves
    
    return reduce(lambda acc, leaf: acc + 1 if leaf == target else acc, leaves, 0)


# dfs 풀이
# dfs
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer