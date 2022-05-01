import sys

input = sys.stdin.readline

RES = 0
N = 33
G = [0 for _ in range(N)]
for i in range(21): G[i] = i+1

G[21] = 21
G[22], G[23], G[24] = 23, 24, 30
G[25], G[26] = 26, 30
G[27], G[28], G[29] = 28, 29, 30
G[30], G[31], G[32] = 31, 32, 20

blueG = dict()
blueG[5], blueG[10], blueG[15] = 22, 25, 27

scores = [0 for _ in range(33)]
for i in range(1, 21): scores[i] = i*2
scores[22], scores[23], scores[24] = 13, 16, 19
scores[25], scores[26] = 22, 24
scores[27], scores[28], scores[29] = 28, 27, 26
scores[30], scores[31], scores[32] = 25, 30, 35

dice = list(map(int, input().split()))
chess = [0 for _ in range(4)]
TRACED = [0 for _ in range(33)]

def dfs(idx, res):
    global RES
    if idx == 10:
        RES = max(RES, res)
        return

    for i in range(4):
        x, x0, move = chess[i], chess[i], dice[idx]

        if x == 5 or x == 10 or x == 15:
            x = blueG[x]
            move -= 1

        for _ in range(move): x = G[x]
        if TRACED[x] and x != 21:
            continue

        TRACED[x0], TRACED[x], chess[i] = 0, 1, x
        dfs(idx + 1, res + scores[x])
        TRACED[x0], TRACED[x], chess[i] = 1, 0, x0

max_ans = 0
dfs(0, 0)
print(RES)
