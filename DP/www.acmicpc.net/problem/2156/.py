import sys

input = sys.stdin.readline
N = int(input())
datas = [int(input()) for _ in range(N)]
DB = [[0,0,0]] + [[0,0,0] for _ in range(N)]

for n in range(N):
    DB[n+1][0] = max(DB[n])
    DB[n+1][1] = DB[n][0] + datas[n]
    DB[n+1][2] = DB[n][1] + datas[n]
        
print(max(DB[-1]))
