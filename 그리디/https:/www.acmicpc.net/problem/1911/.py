import sys, math

input = sys.stdin.readline
N, K = map(int, input().split())
datas = sorted(list(map(int, input().split())) for _ in range(N))
pos, res = datas[0][0], 0

for start, end in datas:
    if start > pos:
        pos = start
    sub_res = math.ceil((end - pos) / K)
    res += sub_res
    pos += sub_res*K
print(res)
