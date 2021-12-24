# https://programmers.co.kr/learn/courses/30/lessons/43165
# dfs 풀이
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

# bfs
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    
    # init
    queue.extendleft([[0, numbers[0]], [0,  numbers[0] * (-1)]])
    
    while len(queue):
        index, value = queue.pop()
        
        if index == len(numbers) - 1:
            answer += 1 if value == target else 0
        else:
            index += 1
            queue.extend([
                [index, value + numbers[index]], 
                [index, value - numbers[index]]])
            
    return answer