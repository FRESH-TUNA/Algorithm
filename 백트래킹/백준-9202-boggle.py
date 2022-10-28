import sys
from itertools import product

D, DR, DC = 8, [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]
N, WIDTH = int(sys.stdin.readline()), 4
WORDS = sorted(sys.stdin.readline().strip() for _ in range(N))
SCORE = [0, 0, 0, 1, 1, 2, 3, 5, 11]
DB = {'word': None}
traced = [[0]*WIDTH for _ in range(WIDTH)]

def inputBoards():
    boards = []
    sys.stdin.readline()
    WORDS_N = int(sys.stdin.readline())
    
    for _ in range(WORDS_N):
        boards.append([sys.stdin.readline().strip() for _ in range(WIDTH)])
        sys.stdin.readline().strip()
    return boards

def makePriorityGraph(board):
    graph = [[[] for c in range(WIDTH)] for r in range(WIDTH)]
    
    for r in range(WIDTH):
        for c in range(WIDTH):
            for d in range(D):
                nr, nc = r+DR[d], c+DC[d]
                if nr==-1 or nr==WIDTH or nc==-1 or nc==WIDTH:
                    continue
                graph[r][c].append((board[nr][nc], nr, nc))

    for r in range(WIDTH):
        for c in range(WIDTH):
            graph[r][c].sort()
    return graph
    
def dbInit():
    for word in WORDS:
        pointer = DB
        for c in word:
            if c not in pointer:
                pointer[c] = {'word': None}
            pointer = pointer[c]
        pointer['word'] = word

def game(board, graph):
    score, longest, count = 0, '', 0

    def check(r, c, pointer, graph):
        nonlocal score, longest, count

        for v, nr, nc in graph[r][c]:
            if v not in pointer or traced[nr][nc]:
                continue
        
            if pointer[v]['word']:
                count += 1
                score += SCORE[len(pointer[v]['word'])]

                if len(pointer[v]['word']) > len(longest):
                    longest = pointer[v]['word']
                pointer[v]['word'] = None
            
            traced[nr][nc] = 1
            check(nr, nc, pointer[v], graph)
            traced[nr][nc] = 0

    nodes = sorted(product(range(WIDTH), repeat=2), 
                   key=lambda x: graph[x[0]][x[1]][0])

    for r, c in nodes:
        if board[r][c] in DB:
            check(r, c, DB, graph)
    return ' '.join((str(score), longest, str(count)))

# driver
for board in inputBoards():
    dbInit()
    print(game(board, makePriorityGraph(board)))

