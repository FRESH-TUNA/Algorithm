import sys
# https://ca.ramel.be/178, ㅊㅏㅁ고자료
# https://suri78.tistory.com/212
# global
res = sys.maxsize

def solution(N, H, ladder):
    dfs(N, H, ladder, 1, 1, 0)
    return res if res < 4 else -1

def dfs(N, H, ladder, i, j, cnt):
    global res
    if check(N, H, ladder): 
        res = min(res, cnt)
        return
    # 브릿지가 3개거나 최적값이 아니면 바로 return
    elif cnt == 3 or res <= cnt: return

    # 가로선
    for x in range(i, H+1):
        # 가로선이 같으면 주어진 세로선 부터 탐색
        k = j if x == i else 1
        # 세로선
        for y in range(k, N):
            if not ladder[x][y] and not ladder[x][y+1]:
                ladder[x][y] = 1
                # 세로선을 이어서 붙이지 못해서 +2 한다
                dfs(N, H, ladder, i, j+2, cnt+1)
                ladder[x][y] = 0
        

# 모든 세로선에 대해 자신의 세로선으로 돌아가는지 check 한다
def check(N, H, ladder):
    for start in range(1, N+1):
        i = start
        for h in range(1, H+1):
            if ladder[h][i]: i += 1
            elif i-1 and ladder[h][i-1]: i -= 1
        if i != start: return False
    return True

# driver
input = sys.stdin.readline
N, M, H = map(int, input().split())
sys.setrecursionlimit(10 ** 6)
# 각 가로선당 세로선
ladder = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    # 가로선 / 세로선
    x, y = map(int, input().split())
    ladder[x][y] = 1
print(solution(N, H, ladder))
