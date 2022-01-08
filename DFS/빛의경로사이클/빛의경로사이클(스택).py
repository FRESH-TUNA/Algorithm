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

def dfs(grid, graph, row, col, direction):
    count = 1
    while True:
        graph[row][col][direction] = True
        direction = next_direction(grid[row][col], direction)
        row, col = next_pos(grid, row, col, direction)
        
        if graph[row][col][direction]: return count
        else: count += 1

def solution(grid):
    answer = []
    grid = [list(row) for row in grid]
    graph = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for row_idx, row in enumerate(graph):
        for col_idx, col in enumerate(row):
            for direction, is_traced in enumerate(col):
                if not is_traced:  
                    answer.append(dfs(grid, graph, row_idx, col_idx, direction))
    
    return sorted(answer)
