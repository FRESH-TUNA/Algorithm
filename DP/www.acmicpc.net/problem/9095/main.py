import sys, heapq

input = sys.stdin.readline
N, DB = int(input()), [0] * 11
DB[1], DB[2], DB[3] = 1, 2, 4

for i in range(4, 11): DB[i] = DB[i-1]+DB[i-2]+DB[i-3]
for _ in range(N): print(DB[int(input())])
