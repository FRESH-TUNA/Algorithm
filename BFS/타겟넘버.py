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
