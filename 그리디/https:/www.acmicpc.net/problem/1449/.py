import sys

input = sys.stdin.readline
N, L = map(int, input().split())
cur, count = 0, 0
datas = sorted(list(map(int, input().split())))

for data in datas:
    if data > cur:
        count += 1
        cur = data+L-1
print(count)
