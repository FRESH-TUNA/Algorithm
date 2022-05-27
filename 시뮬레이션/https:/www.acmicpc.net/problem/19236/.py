import sys

# global
input = sys.stdin.readline
FISH_N, SHARK, N, DELETED = 16, 0, 4, -1
I, J, D, ND = 0, 1, 2, 8
AD = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
FISHES, G = [None]*(FISH_N+1), [None]*N
Answer = 0

# init
for i in range(N):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().split())
    G[i] = [a0, a1, a2, a3]
    FISHES[a0], FISHES[a1] = [i, 0, b0-1], [i, 1, b1-1]
    FISHES[a2], FISHES[a3] = [i, 2, b2-1], [i, 3, b3-1]

# solution
def solution():
    # root init
    root_fish = G[0][0]
    FISHES[SHARK] = [0, 0, FISHES[root_fish][D]]
    answer = root_fish
    FISHES[root_fish] = None
    G[0][0] = SHARK

    simulate(FISHES, G, answer)
    return Answer

def simulate(fishes, g, answer):
    global Answer
    for fish in range(1, FISH_N+1):
        if fishes[fish]: fish_move(fishes, g, fish)

    i, j, d = fishes[SHARK]
    ci, cj = AD[d]
    ni, nj = i, j

    while True:
        ni, nj = ni+ci, nj+cj
        
        if out_of_range(ni, nj): 
            Answer = max(Answer, answer)
            break

        eaten = g[ni][nj]
        if eaten == DELETED: continue

        ng = [[c for c in row] for row in g]
        nfishes = [[data for data in fish] if fish else None for fish in fishes]

        ng[ni][nj], ng[i][j] = SHARK, DELETED
        nfishes[SHARK], nfishes[eaten] = nfishes[eaten], None
        simulate(nfishes, ng, answer+eaten)

def fish_move(fishes, g, fish):
    i, j, d = fishes[fish]

    for _ in range(ND):
        ci, cj = AD[d]
        ni, nj = i+ci, j+cj

        if out_of_range(ni, nj) or g[ni][nj] == SHARK:
            d = (d+1)%8
            continue  
        fishes[fish][I], fishes[fish][J], fishes[fish][D] = ni, nj, d

        changed_fish = g[ni][nj]
        if changed_fish != DELETED:
            fishes[changed_fish][I], fishes[changed_fish][J] = i, j
        g[i][j], g[ni][nj] = changed_fish, fish
        return
        
def out_of_range(i, j):
    return i==-1 or i==N or j==-1 or j==N

print(solution())
