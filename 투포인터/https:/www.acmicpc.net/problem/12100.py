# global
ans=0
MAX_DEPTH=5

def move(graph, d):
    N = len(graph)

    # 0, 1, 2, 3 (상, 하, 좌, 우)
    if d == 0:
        for j in range(N):
            top = 0
            for i in range(1, N):
                if graph[i][j]:
                    v = graph[i][j] 
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                       graph[top][j] = v
                    elif graph[top][j] == v:
                        graph[top][j] = v*2
                        top += 1
                    else:
                        top += 1
                        graph[top][j] = v
    if d == 1:
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if graph[i][j]:
                    v = graph[i][j] 
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                        graph[top][j] = v
                    elif graph[top][j] == v:
                        graph[top][j] = v*2
                        top -= 1
                    else:
                        top -= 1
                        graph[top][j] = v
    if d == 2:
        for i in range(N):
            top = 0
            for j in range(1, N):
                if graph[i][j]:
                    v = graph[i][j] 
                    graph[i][j] = 0
                    if graph[i][top] == 0:
                        graph[i][top] = v
                    elif graph[i][top] == v:
                        graph[i][top] = v*2
                        top += 1
                    else:
                        top += 1
                        graph[i][top] = v
    if d == 3:
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if graph[i][j]:
                    v = graph[i][j] 
                    graph[i][j] = 0
                    if graph[i][top] == 0:
                        graph[i][top] = v
                    elif graph[i][top] == v:
                        graph[i][top] = v*2
                        top -= 1
                    else:
                        top -= 1
                        graph[i][top] = v

def dfs(graph, depth):
    global ans
    N = len(graph)
    if depth == MAX_DEPTH:
        for i in range(N):
            for j in range(N):
                ans = max(ans, graph[i][j])
        return

    for d in range(4):
        # copy
        _graph = [[c for c in r] for r in graph]
        move(_graph, d)
        dfs(_graph, depth+1)

# driver
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dfs(graph, 0)
print(ans)
