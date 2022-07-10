import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    C, R = deque(list(map(int, input().split()))), deque([0]*N)
    answer, k = 0, 0

    while True:
        C.rotate(1)
        R.rotate(1)
        R[-1] = 0
        
        if sum(R):
            # 가장 마지막위치가 가장 먼저 로봇이 들어간 위치가 될수 있다.
            for i in range(N-2, -1, -1):
                if R[i] == 1 and R[i+1] == 0 and C[i+1] >= 1:
                    R[i+1], R[i] = 1, 0
                    C[i+1] -= 1
                    k += [0,1][C[i+1] == 0]
            # 마지막 위치의 로봇은 항상 삭제된다.
            R[-1]=0

        # 첫번째 자리에 로봇 적재 시도
        if R[0]==0 and C[0]>=1:
            R[0] = 1
            C[0] -= 1
            k += [0,1][C[0] == 0]  
        
        answer += 1
        if k >= K: break 
            
    print(answer)

solution()
