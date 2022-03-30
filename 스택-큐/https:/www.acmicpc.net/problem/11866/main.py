import sys
from collections import deque

# global
input = sys.stdin.readline
N, K = 0, 0

def solution():
    DB, RES = deque(i for i in range(1, N+1)), []
    counter = 0
    
    while DB:
        counter += 1
        element = DB.popleft()
        if counter == K: 
            RES.append(element)
            counter = 0
        else: DB.append(element)
    print('<' + ', '.join(str(x) for x in RES) + '>')
        
    
# driver
N, K = map(int, input().split())
solution()
