import sys
 
# init
input = sys.stdin.readline
DATAS = [list(map(int, input().rstrip().split())) for _ in range(int(input()))]
 
def solutions():
    for DATA in DATAS:
        print("YES" if solution(*DATA) else "NO")
 
def solution(a, b, c, x, y):
    if a + c < x: return False
    x -= a
    if x > 0: c -= x
    return (b + c) >= y
 
solutions()
