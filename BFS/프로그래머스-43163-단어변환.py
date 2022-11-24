from collections import deque, defaultdict
import heapq

# 깊이 우선탐색으로 풀꺼면 너비우선탐색, 다익스트라 도 고려해봐야 한다.
# 왜냐하면 깊이우선탐색이면 그래프문제라는것이고
# 더 시간짧은 너비우선탐색, 다익스트라인것을 고려해야 한다.

# bfs
# def solution(begin, target, words):
#     DISTANCE = len(words)+1
#     distances = defaultdict(lambda: DISTANCE)
    
#     q = deque()
#     q.append((0, begin))
#     distances[begin] = 0
    
#     while q:
#         dist, current = q.popleft()
#         if current == target:
#             return dist
        
#         for word in words:
#             if distances[word]==DISTANCE and canChange(current, word):
#                 distances[word] = dist+1
#                 q.append((dist+1, word))
#     return 0
    
# def canChange(a, b):
#     diff = 0
    
#     for (c, d) in zip(a, b):
#         if c!=d:
#             diff += 1
#         if diff==2:
#             return False
#     return True

# dijkstra
def solution(begin, target, words):
    DISTANCE = len(words)+1
    distances = defaultdict(lambda: DISTANCE)
    
    q = []
    heapq.heappush(q, (0, begin))
    distances[begin] = 0
    
    while q:
        dist, current = heapq.heappop(q)
        
        if dist > distances[current]:
            continue
        
        for word in words:
            if distances[word] > distances[current]+1 and canChange(current, word):
                distances[word] = distances[current]+1
                heapq.heappush(q, (distances[word], word))
    return 0 if distances[target]==DISTANCE else distances[target]
    
def canChange(a, b):
    diff = 0
    
    for (c, d) in zip(a, b):
        if c!=d:
            diff += 1
        if diff==2:
            return False
    return True

