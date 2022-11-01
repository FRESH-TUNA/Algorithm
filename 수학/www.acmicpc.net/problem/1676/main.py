import sys

input = sys.stdin.readline
n, count = int(input()), 0

while n:
    n //= 5
    count += n

print(count)
