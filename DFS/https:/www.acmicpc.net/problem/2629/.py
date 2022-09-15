import sys

input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))
M = int(input())
candidates = list(map(int, input().split()))
possible = []
answer = [[0]*15001 for i in range(N+1)]

def scale(now,left,right):
    new = abs(left-right)

    if new not in possible:
        possible.append(new)
    if now == N:
        return
    if answer[now][new] == 0:
        answer[now][new] = 1
        
        # 저울의 왼쪽에 놓는경우
        scale(now+1,left+rocks[now],right)

        # 저울의 오른쪽에 놓는경우
        scale(now+1,left,right+rocks[now])

        # 저울에 아예 안놓는경우
        scale(now+1,left,right)

def call():
    scale(0,0,0)

    for candidate in candidates:
        if candidate in possible:
            print("Y", end=' ')
        else:
            print("N", end=' ')
call()

