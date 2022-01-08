# 재귀방식으로 solve시 반드시 추가
# https://programmers.co.kr/learn/courses/30/lessons/86052

# 재귀방식으로 solve시 반드시 추가
import sys
sys.setrecursionlimit(10 ** 6)

def next_direction(node_type, direction):
    next_directions = {
        "S": [0, 1, 2, 3], "L": [3, 0, 1, 2], "R": [1, 2, 3, 0]}
    return next_directions[node_type][direction]

def next_pos(grid, row, col, direction):
    m_row, m_col = len(grid) - 1, len(grid[0]) - 1
    row, col = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)][direction]
    row = m_row if row < 0 else (0 if row == m_row + 1 else row)
    col = m_col if col < 0 else (0 if col == m_col + 1 else col)
    return [row, col]

def dfs(grid, graph, row, col, direction, count):
    # traced 처리
    if graph[row][col][direction]: return count
    else: graph[row][col][direction] = True
    
    # next direction
    direction = next_direction(grid[row][col], direction)
    
    # 다음 원소 결정 및 보정
    row, col = next_pos(grid, row, col, direction)
    return dfs(grid, graph, row, col, direction, count + 1)
    
def solution(grid):
    answer = []
    grid = [list(row) for row in grid]
    graph = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for row_idx, row in enumerate(graph):
        for col_idx, col in enumerate(row):
            for direction, is_traced in enumerate(col):
                if not is_traced:  
                    answer.append(dfs(grid, graph, row_idx, col_idx, direction, 0))
    
    return sorted(answer)
