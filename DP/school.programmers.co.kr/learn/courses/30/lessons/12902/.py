def solution(n):
    answer = 0
    dp, dp[0] = [0] * (n + 1), 1

    special = 0
    for i in range(2, n+1, 2):
        dp[i] = (dp[i-2] * 3 + special * 2) % 1000000007
        special += dp[i-2]
        
    return dp[n]
