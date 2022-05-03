import sys, math

input = sys.stdin.readline
N = int(input())
datas = [input().rstrip() for _ in range(N)]

def check(d, right):
    left = 0
    while left < right:
        if d[left] == d[right]: return False
        else:
            left += 1
            right -= 1
    return True            

def solutions():
    for d in datas:
        flag = True
        right_border = len(d) + 1
        while right_border != 2:
            if not check(d, right_border-2):
                flag = False
                break
            right_border = right_border // 2
        print("YES" if flag else "NO")

solutions()
