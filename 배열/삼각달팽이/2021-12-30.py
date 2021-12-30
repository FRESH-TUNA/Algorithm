def solution(n):
    matrix = [[0] * (i + 1) for i in range(n)]
    directions = ((1, 0), (0, 1), (-1, -1))
    d_idx, x, y, value = 0, -1, 0, 0
    
    while n:
        i_x, i_y  = directions[d_idx]
        for _ in range(n):
            x, y, value = x + i_x, y + i_y, value + 1
            matrix[x][y] = value
        n, d_idx = n - 1, (d_idx + 1) % 3

    return [v for row in matrix for v in row]
