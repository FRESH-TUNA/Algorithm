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


# 내풀이인데 안된다
def bfs(numbers, target):
    answer = 0
    queue = [[0, numbers[0]], [0, numbers[0] * (-1)]]
    
    while queue:
        pointer, result = queue.pop()
        if len(numbers) - 1 == pointer:
            answer += (1 if result == target else 0)
        else:
            pointer += 1
            queue = [
                [pointer, result + numbers[pointer]],
                [pointer, result - numbers[pointer]]
            ] + queue
    return answer

def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer