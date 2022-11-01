import sys

# global
input = sys.stdin.readline
N, M, K = 0, 0, 0

def solution():
    print(pow(N, M))

def pow(n, e):
    if e == 1: return n % K
    subres = pow(n, e // 2)
    if e % 2 == 1:	
        return (subres * subres % M) * n % K
    return subres * subres % K

# driver
N, M, K = map(int, input().split())
solution()