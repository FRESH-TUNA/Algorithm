from sys import stdin

def solution(coins, target):
    ans, ans[0] = [0] * (target+1), 1

    for coin in coins:
        for i in range(coin, n+1):
            ans[i] += ans[i-coin]

    return ans[-1]

# driver
n, target = map(int, stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(stdin.readline()))
print(solution(coins, k))
