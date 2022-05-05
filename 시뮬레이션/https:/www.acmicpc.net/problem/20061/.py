import sys

# init
input = sys.stdin.readline
BORDER = 10
G = [[0]*BORDER for _ in range(BORDER)]
DATAS = [list(map(int, input().rstrip().split())) for _ in range(int(input()))]
RES = 0

def solution():
    for t, x, y in DATAS:
        if t == 1: gaming([[x, y]])
        elif t == 2: gaming([[x, y], [x, y+1]])
        else: gaming([[x, y], [x+1, y]])

    blocks = 0
    for row in G:
        for x in row:
            if x == 1: blocks += 1
    print(RES)
    print(blocks)
    

def gaming(blocks):
    blue_move(blocks); green_move(blocks);
    blue_remove(); green_remove();
    blue_shift(); green_shift();

# move
def blue_move(blocks):
    blocks = [[x, y] for x, y in blocks]
    while True:
        if blue_border_check(blocks):
            for x, y in blocks: G[x][y] = 1
            # print("---")
            #for i in range(10): print(G[i])
            return
        for i in range(len(blocks)):
            blocks[i][1] += 1

def green_move(blocks):
    while True:
        if green_border_check(blocks):
            for x, y in blocks: G[x][y] = 1
            return
        for i in range(len(blocks)):
            blocks[i][0] += 1


# remove
def blue_remove():
    global RES
    b, p = BORDER-1, BORDER-1

    while p >= 0 and b >= 0:
        if G[0][p] and G[1][p] and G[2][p] and G[3][p]:
            RES += 1
        else:
            G[0][b], G[1][b] = G[0][p], G[1][p]
            G[2][b], G[3][b] = G[2][p], G[3][p]
            b -= 1
        p -= 1

    for i in range(b+1):
        G[0][i] = G[1][i] = G[2][i] = G[3][i] = 0
    # print("---")
    # for i in range(10): print(G[i])

def green_remove():
    global RES
    b, p = BORDER-1, BORDER-1

    while p >= 0 and b >= 0:
        if G[p][0] and G[p][1] and G[p][2] and G[p][3]:
            RES += 1
        else:
            G[b][0], G[b][1] = G[p][0], G[p][1]
            G[b][2], G[b][3] = G[p][2], G[p][3]
            b -= 1
        p -= 1

    for i in range(b+1):
        G[i][0] = G[i][1] = G[i][2] = G[i][3] = 0
    # print("---")
    # for i in range(10): print(G[i])


# shift
def blue_shift():
    n = 0
    if G[0][4] or G[1][4] or G[2][4] or G[3][4]: n += 1
    if G[0][5] or G[1][5] or G[2][5] or G[3][5]: n += 1

    if n == 0:
        # print("---")
        # for i in range(10): print(G[i])
        return
    for i in range(BORDER-1-n, -1, -1):
        G[0][i+n], G[1][i+n] = G[0][i], G[1][i]
        G[2][i+n], G[3][i+n] = G[2][i], G[3][i]

    for i in range(n):
        G[0][i] = G[1][i] = G[2][i] = G[3][i] = 0
    # print("---")
    # for i in range(10): print(G[i])

def green_shift():
    n = 0
    if G[4][0] or G[4][1] or G[4][2] or G[4][3]: n += 1
    if G[5][0] or G[5][1] or G[5][2] or G[5][3]: n += 1

    if n == 0:
        # print("---")
        # for i in range(10): print(G[i])
        return
    for i in range(BORDER-1-n, -1, -1):
        G[i+n][0], G[i+n][1] = G[i][0], G[i][1]
        G[i+n][2], G[i+n][3] = G[i][2], G[i][3]

    for i in range(n):
        G[i][0] = G[i][1] = G[i][2] = G[i][3] = 0
    # print("---")
    # for i in range(10): print(G[i])

# border check
def blue_border_check(blocks):
    for x, y in blocks:
        if y == BORDER-1 or G[x][y+1]: return True
    return False

def green_border_check(blocks):
    for x, y in blocks:
        if x == BORDER-1 or G[x+1][y]: return True
    return False
    
solution()