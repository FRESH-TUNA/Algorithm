import sys
i = sys.stdin.readline
i()
A, B = sorted(map(int, i().split())), sorted(map(int, i().split()), reverse=True)
print(sum(x[0]*x[1] for x in zip(A, B)))
