import sys, math

# init
input = sys.stdin.readline
BORDER = 10
G = [[0]*BORDER for _ in range(BORDER)]


def solution():
    edges = sorted([(datas[i], datas[i+1]) for i in range(len(datas)-1)], 
                key=lambda x: x[1]-x[0], reverse=True)
    res, count = datas[-1] - datas[0], 1

    for x, y in edges:
        if count >= T: break
        count += 1
        res -= (y-x)
    print(res)


def blue_postprocessing():
    

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
