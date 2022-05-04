import sys, math

# init
input = sys.stdin.readline
BORDER = 10
G = [[0]*BORDER for _ in range(BORDER)]
N = int(input())
DATAS = [list(map(int, input().rstrip().split())) for _ in range(N)]

def solution():
    edges = sorted([(datas[i], datas[i+1]) for i in range(len(datas)-1)], 
                key=lambda x: x[1]-x[0], reverse=True)
    res, count = datas[-1] - datas[0], 1

    for x, y in edges:
        if count >= T: break
        count += 1
        res -= (y-x)
    print(res)

def blue_remove():
    b, p = N-1, N-1

    while p >= 0:
        if G[0][p] and G[1][p] and G[2][p] and G[3][p]:
            p -= 1
        else:
            G[0][b], G[1][b] = G[0][p], G[1][p]
            G[2][b], G[3][b] = G[2][p], G[3][p]
            b -= 1

    for i in range(b+1):
        G[0][i] = G[1][i] = G[2][i] = G[3][i] = 0
    
def blue_shift():
    n = 0
    if G[0][4] or G[1][4] or G[2][4] or G[3][4]: n += 1
    if G[0][5] or G[1][5] or G[2][5] or G[3][5]: n += 1

    for i in range(N-1-n, -1, -1):
        G[0][i+n], G[1][i+n] = G[0][i], G[1][i]
        G[2][i+n], G[3][i+n] = G[2][i], G[3][i]

    for i in range(n):
        G[0][i] = G[1][i] = G[2][i] = G[3][i] = 0
        

    
def blue_border_check(blocks):
    for x, y in blocks:
        if y == BORDER-1 or G[x][y+1]: return True
    return False
            
def blue_move(blocks):
    while True:
        if blue_border_check(blocks):
            for x, y in blocks:
                G[x][y] = 1
                return
        for i in range(len(blocks)):
            blocks[i][1] += 1 
        
def green_border_check(blocks):
    for x, y in blocks:
        if x == BORDER-1 or G[x+1][y]: return True
    return False
            
def green_move(blocks):
    while True:
        if green_border_check(blocks):
            for x, y in blocks:
                G[x][y] = 1
                return
        for i in range(len(blocks)):
            blocks[i][0] += 1 
        
        
    
solution()
