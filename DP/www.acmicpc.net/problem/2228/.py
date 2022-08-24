import sys

input = sys.stdin.readline
N, M = map(int, input().split())
CDB = [[0]+[-32769]*M for i in range(N+1)]
NDB = [[0]+[-32769]*M for i in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min(M, (i+1)//2)+1):
        NDB[i][j] = max(CDB[i-1][j], NDB[i-1][j])
        CDB[i][j] = max(CDB[i-1][j], NDB[i-1][j-1])+num
print(max(CDB[N][M], NDB[N][M]))
