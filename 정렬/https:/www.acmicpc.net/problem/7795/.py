import sys, bisect
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = input().split()   
    ns = list(map(int, input().split()))
    ms = sorted(list(map(int, input().split())))
    res = 0

    for n in ns:
        res += (bisect.bisect_left(ms, n))
    print(res)
    