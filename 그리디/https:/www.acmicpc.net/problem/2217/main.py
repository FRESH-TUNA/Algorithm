import sys
i = sys.stdin.readline
N = int(i())
V = zip(range(N, -1, -1), sorted(int(i()) for _ in range(N)))
print(max(x[0]*x[1] for x in V))
