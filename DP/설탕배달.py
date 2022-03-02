def solution(n):
    ans, ans[1], ans[2] = [0] * (n+1), -1, -1

    for i in range(3, n+1):
        if i >= 5 and ans[i-5]: ans[i] += ans[i-1] + 1
        elif ans[i-3]: ans[i] += ans[i-3] + 1
        else: ans[i] = -1
    
    return ans[-1]

# driver
print(solution(int(input())))
