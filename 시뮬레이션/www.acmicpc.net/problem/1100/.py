import sys

input = sys.stdin.readline
N = 8
G = [list(input().rstrip()) for _ in range(8)]
answer = 0

for i in range(N):
    for j in range(N):
        answer += ((i+j)%2 == 0 and G[i][j]=="F")
print(answer)

