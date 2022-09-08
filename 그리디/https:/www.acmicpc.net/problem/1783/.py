from sys import stdin

R, C = map(int, stdin.readline().split())

if R == 1:
    print(1)
elif R == 2:
    print(min(4, (C+1)//2))
else:
    if C <= 6:
        print(min(4, C))
    else:
        print(C-2)
