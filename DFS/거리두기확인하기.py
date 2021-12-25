# https://programmers.co.kr/learn/courses/30/lessons/81302

ROW, COL = 5, 5

def dfs(place, is_traced, row, col, depth):
    checkpoints = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    parent_status = place[row][col]
    # 부모 체크
    is_traced[row][col] = True
    
    for x, y in checkpoints:
        x_c, y_c = row + x, col + y
              
        # in range check
        if not(x_c >= 0 and x_c < ROW and y_c >= 0 and y_c < COL): continue
                   
        # traced check (자식 체크)
        if is_traced[x_c][y_c]: continue         
        else: is_traced[x_c][y_c] = True
            
        # 거리두기 check
        if place[x_c][y_c] == "P" and parent_status != "X": return False
        
        # 다음 dfs 실행 여부        
        if depth < 2 and not dfs(place, is_traced, x_c, y_c, depth + 1):
            return False

    return True
        
def checked(place):
    place = [list(row) for row in place]
    
    # trace
    for row in range(ROW):
        for col in range(COL):
            if place[row][col] == "P" and not dfs(place, [[False for _ in range(COL)] for _ in range(ROW)], row, col, 1):
                return 0
    return 1

def solution(places):
    return [checked(place) for place in places]
