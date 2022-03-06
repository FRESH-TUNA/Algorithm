from sys import stdin
def solution(N, GRAPH):
    ans, ans[0][0] = [[0] * N for _ in range(N)], 1
    
    for i in range(N):
        for j in range(N):
            jump = GRAPH[i][j]
            if jump and ans[i][j]:
                if i + jump < N: ans[i + jump][j] += ans[i][j]
                if j + jump < N: ans[i][j + jump] += ans[i][j]
    
    return ans[-1][-1]

# driver
N = int(stdin.readline())
GRAPH = [list(map(int, stdin.readline().split())) for _ in range(N)]
print(solution(N, GRAPH))
