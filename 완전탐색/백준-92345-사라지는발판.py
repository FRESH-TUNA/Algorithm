def get_next_positions(board, r, c):
    R, C = [0, 0, 1, -1], [1, -1, 0, 0]
    next_positions = []
    
    for d in range(4):
        nr, nc = r+R[d], c+C[d]
        if nr==-1 or nc==-1 or nr==len(board) or nc==len(board[0]):
            continue
        if board[nr][nc] == 0:
            continue
        next_positions.append((nr, nc))
    return next_positions


def search(board, aloc, bloc, turn):
    current = (turn%2==0)
    r, c = aloc if current==True else bloc
    next_positions = get_next_positions(board, r, c)

    if not next_positions:  
        return (not current, turn)

    if aloc==bloc:
        return current, turn+1
    
    win, lose = [], []
    board[r][c] = 0

    for nr, nc in next_positions:
        if current:
            winner, count = search(board, [nr, nc], bloc, turn + 1)
        else:
            winner, count = search(board, aloc, [nr, nc], turn + 1)
        
        if current==winner:
            win.append(count)
        else:
            lose.append(count)
    board[r][c] = 1
                  
    return (current, min(win)) if win else (not current, max(lose))


def solution(board, aloc, bloc):
    winner, answer = search(board, aloc, bloc, 0)
    return answer
