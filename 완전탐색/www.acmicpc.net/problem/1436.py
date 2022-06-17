import sys

input = sys.stdin.readline

d = int(input())
current = 665

while d:
    current += 1
    if '666' in str(current): d -= 1

print(current)
