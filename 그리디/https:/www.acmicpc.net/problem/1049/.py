import sys

input = sys.stdin.readline

N, M = map(int, input().split())
single, package = 100000, 100000
divided, remain = N//6, N%6

for _ in range(M):
    p, s = map(int, input().split())
    single = min(single, s, p)
    package = min(package, p, s*6)

print(divided*package + min(package, remain*single))

