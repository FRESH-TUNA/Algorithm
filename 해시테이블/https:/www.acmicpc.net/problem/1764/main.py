import sys

input = sys.stdin.readline
N, M = map(int, input().split())
DB, res = set(), list()

for _ in range(N): DB.add(input().rstrip())
for _ in range(M): 
    key = input().rstrip()
    if key in DB: res.append(key)

print(len(res))
for word in sorted(res): print(word)
