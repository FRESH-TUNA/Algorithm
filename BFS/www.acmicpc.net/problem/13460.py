from collections import deque
import sys

def bfs(rx, ry, bx, by, graph):
    Q = deque()
    visited = set()
    count = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

    Q.append((rx, ry, bx, by))
    while Q:
        for _ in range(len(Q)):
            rx, ry, bx, by = Q.popleft()
            if count > 10: return -1
            if graph[rx][ry] == 'O': return count
            for d in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[d]
                    nry += dy[d]
                    if graph[nrx][nry] == '#':
                        nrx -= dx[d]
                        nry -= dy[d]
                        break
                    if graph[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx[d]
                    nby += dy[d]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[d]
                        nby -= dy[d]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                if graph[nbx][nby] == 'O': continue

                if nrx == nbx and nry == nby:
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                        nrx -= dx[d]
                        nry -= dy[d]
                    else:
                        nbx -= dx[d]
                        nby -= dy[d]
            
                if (nrx, nry, nbx, nby) not in visited:
                    Q.append((nrx, nry, nbx, nby))
                    visited.add((nrx, nry, nbx, nby))
        count += 1
    return -1
            
 
# driver
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by, graph))

