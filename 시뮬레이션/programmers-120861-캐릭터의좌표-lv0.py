def solution(keyinputs, board):
    r, c = 0, 0
    R, C = board[0]//2, board[1]//2
    DR, DC = {"up":0, "down":0, "left":-1, "right":1}, {"up":1, "down":-1, "left":0, "right":0}
    
    for keyinput in keyinputs:
        nr, nc = r+DR[keyinput], c+DC[keyinput]
        if abs(nr)==(R+1) or abs(nc)==(C+1):
            continue
        r, c = nr, nc
    return [r, c]

