import sys

input = sys.stdin.readline

def answer(N, coins, target):
    coins = [0]+coins
    DB = [0]*(target+1)

    DB[0] = 1
    for c in range(1, N+1):
        for t in range(coins[c], target+1):
            DB[t] += DB[t-coins[c]]
    return DB[target]

def call():
    for _ in range(int(input())):
        N = int(input())
        coins = list(map(int, input().split()))
        target = int(input())
        print(answer(N, coins, target))
call()
