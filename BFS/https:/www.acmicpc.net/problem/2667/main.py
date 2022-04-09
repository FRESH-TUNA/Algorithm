from collections import deque

N = int(input())
G = [list(map(int, list(input())[:N])) for _ in range(N)]
RES, TRACED, BORDER = [], 2, 0

def bfs(i, j):
    Q, res, G[i][j] = deque(), 1, TRACED
    Q.append((i, j))

    while Q:
        i, j = Q.pop()
        for (ni, nj) in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if ni in (-1, N) or nj in (-1, N): continue
            if G[ni][nj] in (TRACED, BORDER): continue
            res, G[ni][nj] = res + 1, TRACED
            Q.appendleft((ni, nj))
    return res


# driver
for i in range(N):
    for j in range(N):
        if G[i][j] not in (TRACED, BORDER):
            RES.append(bfs(i, j))
print(len(RES))
print('\n'.join(str(res) for res in sorted(RES)))
