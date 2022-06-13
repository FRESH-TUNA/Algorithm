import sys

def solution(N, G):
    SLASH, BACKSLASH, TYPE = [0]*(2*N+1), [0]*(2*N+1), 2
    answer = [0]
    datas = []
    
    def init():
        for i in range(N):
            for j in range(N):
                if G[i][j]:
                    datas.append((i, j))
        
    def dfs(start, ans):
        answer[0] = max(answer[0], ans)

        for s in range(start, len(datas)):
            ni, nj = datas[s]
            nslash, nbackslash = ni+nj, ni-nj+N

            if SLASH[nslash] or BACKSLASH[nbackslash]:
                continue  
            SLASH[nslash] = BACKSLASH[nbackslash] = 1
            dfs(s+1, ans+1)
            SLASH[nslash] = BACKSLASH[nbackslash] = 0

    def call():
        init()
        dfs(0, 0)
        return answer[0]

    return call()

# driver
input = sys.stdin.readline
N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, G))
