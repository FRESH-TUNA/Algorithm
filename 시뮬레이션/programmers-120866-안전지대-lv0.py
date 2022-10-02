def solution(board):
    N = len(board)
    D, DR, DC = 8, (-1,-1,0,1,1,1,0,-1), (0,1,1,1,0,-1,-1,-1)
    NEW_BOARD = [[0]*(N+2) for _ in range(N+2)]
    SAFE, BOMB, NON_SAFE = 0, 1, 2
    
    def init():
        for i in range(1, N+1):
            for j in range(1, N+1):
                NEW_BOARD[i][j] = board[i-1][j-1]
    
    def check():
        for i in range(1, N+1):
            for j in range(1, N+1):
                if NEW_BOARD[i][j] == BOMB:
                    for d in range(D):
                        ni, nj = i+DR[d], j+DC[d]
                        NEW_BOARD[ni][nj] = [NON_SAFE, BOMB][NEW_BOARD[ni][nj]==BOMB]
    
    def answer():
        result = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                result += [0,1][NEW_BOARD[i][j]==SAFE]
        return result

    init()
    check()
    return answer()

