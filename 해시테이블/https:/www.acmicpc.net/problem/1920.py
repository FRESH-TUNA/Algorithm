import sys

# driver
input = sys.stdin.readline
_, data = input(), set(input().rstrip().split())
_, target = input(), input().rstrip().split()
print('\n'.join('1' if x in data else '0' for x in target))
