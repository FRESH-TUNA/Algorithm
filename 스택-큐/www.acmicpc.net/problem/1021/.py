from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ELEMENTS = list(map(int, input().split()))
Q = deque(n for n in range(1, N+1))

count = 0
for e in ELEMENTS:
    while True:
        if Q[0] == e:
            Q.popleft()
            break
        else:
            if Q.index(e) < len(Q)/2:
                while Q[0] != e:
                    Q.append(Q.popleft())  
                    count += 1
            else:   
                while Q[0] != e:
                    Q.appendleft(Q.pop())  
                    count += 1
print(count)

