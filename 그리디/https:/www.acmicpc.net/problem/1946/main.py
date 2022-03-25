import sys
i = sys.stdin.readline

for _ in range(int(i())):
    data = [list(map(int, i().split())) for _ in range(int(i()))]
    minimum, res = len(data)+1, 0
    for (_, b) in sorted(data):
        if b < minimum: 
            res += 1
            minimum = b
    print(res)
