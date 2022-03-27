import sys, heapq, math
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
DB = dict()

for i in range(1, N+1):
    key = str(i)
    DB[key] = input().rstrip()
    DB[DB[key]] = key

for _ in range(M): print(DB[input().rstrip()])
