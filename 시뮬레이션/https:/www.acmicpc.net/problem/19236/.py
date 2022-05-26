import sys

# global
input = sys.stdin.readline
FISH_N, SHARK, N, DELETED = 16, 0, 4, -1
I, J, D, ND = 0, 1, 2, 8
AD = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
FISHES, G = [None]*(FISH_N+1), [None]*N

# init
for i in range(N):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().split())
    G[i] = [a0, a1, a2, a3]
    FISHES[a0], FISHES[a1] = [i, 0, b0-1], [i, 1, b1-1]
    FISHES[a2], FISHES[a3] = [i, 2, b2-1], [i, 3, b3-1]

# solution
def solution():
    answer = 0

    # root
    root_fish = G[0][0]
    FISHES[SHARK] = [0, 0, FISHES[root_fish][D]]
    answer += root_fish
    FISHES[root_fish] = None
    G[0][0] = SHARK
    
    while True:
        for fish in range(1, FISH_N+1):
            if FISHES[fish]: fish_move(fish)
        score = shark_move()
        if not score: break
        answer += score

    return answer
    
def fish_move(fish):
    fish_i, fish_j, fish_d = FISHES[fish]
    for _ in range(ND):
        ci, cj = AD[fish_d]
        nfish_i, nfish_j = fish_i+ci, fish_j+cj

        if out_of_range(nfish_i, nfish_j):
            fish_d = (fish_d+1)%8
            continue

        changed_fish = G[nfish_i][nfish_j]
        if changed_fish == SHARK:
            fish_d = (fish_d+1)%8
            continue

        FISHES[fish][I], FISHES[fish][J], FISHES[fish][D] = nfish_i, nfish_j, fish_d
        if changed_fish != DELETED:
            FISHES[changed_fish][I], FISHES[changed_fish][J] = fish_i, fish_j
        G[fish_i][fish_j], G[nfish_i][nfish_j] = G[nfish_i][nfish_j], G[fish_i][fish_j]
        return

def shark_move():
    i, j, d = FISHES[SHARK]
    ci, cj = AD[d]
    si, sj = i, j
    ni, nj = i, j
    score = 0

    while True:
        ni, nj = ni+ci, nj+cj
        
        if out_of_range(ni, nj): break
        
        fish = G[ni][nj]
        if G[ni][nj] == DELETED: continue

        if fish > score:
            score = max(fish, score)
            si, sj = ni, nj

    if i != si or j != sj:
        G[si][sj] = G[i][j]
        G[i][j] = DELETED
        FISHES[SHARK] = FISHES[score]
        FISHES[score] = None
    return score
        
def out_of_range(i, j):
    return i<0 or i==N or j<0 or j==N

print(solution())