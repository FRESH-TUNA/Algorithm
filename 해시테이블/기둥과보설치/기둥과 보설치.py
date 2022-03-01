def solution(n, build_frame):
    # 기둥: 0, 보: 1
    answer, graph = set(), [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

    for (x, y, bow, install) in build_frame:
        result = False
        if bow and install: result = set_bow(graph, x, y)
        elif bow and not install: result = deset_bow(graph, x, y)
        elif not bow and install: result = set_gidung(graph, x, y)
        else: result = deset_gidung(graph, x, y)
        if result and install: answer.add((x, y, bow))
        if result and not install: answer.remove((x, y, bow))

    return sorted(list(answer))
        
def set_bow(graph, x, y):
    print("set_bow", x, y)
    #bow와 bow 사이
    if (x-1 >= 0 and graph[x-1][y][1] and 
        x+1 < len(graph) and graph[x+1][y][1]):
        graph[x][y][1] = 1
    
    #밑에 기둥이 있는가
    if y-1 >= 0 and graph[x][y-1][0]: graph[x][y][1] = 1
    if x+1 < len(graph) and y-1 >= 0 and graph[x+1][y-1][0]:
        graph[x][y][1] = 1
    return graph[x][y][1] == 1
    
def deset_bow(graph, x, y):
    print("deset_bow", x, y)
    # 밑에 기둥이 있으면
    if x+1 < len(graph) and y-1 >= 0 and graph[x+1][y-1][0]:
        graph[x][y][1] = 0
    
    return graph[x][y][1] == 0

def set_gidung(graph, x, y):
    print("set_gidung", x, y)
    # 바닥
    if not y: graph[x][y][0] = 1
    
    # 보위에 있는가?
    if x-1 >= 0 and graph[x-1][y][1]: graph[x][y][0] = 1
    if graph[x][y][1]: graph[x][y][0] = 1

    # 기둥위에 있는가?
    if y-1 >= 0 and graph[x][y-1][0]: graph[x][y][0] = 1   
    
    return graph[x][y][0] == 1
    
def deset_gidung(graph, x, y):
    #bow와 bow 사이
    if (x-1 >= 0 and y+1 < len(graph) and 
        graph[x-1][y+1][1] and graph[x][y+1][1]):
        graph[x][y][0] = 0
    print("deset_gidung", x, y)
    return graph[x][y][0] == 0