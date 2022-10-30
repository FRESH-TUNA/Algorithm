import sys
from itertools import product
from functools import cmp_to_key

D, DR, DC = 8, [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]
N, WIDTH = int(sys.stdin.readline()), 4
WORDS = [sys.stdin.readline().strip() for _ in range(N)]
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

def dbInit():
    for word in WORDS:
        pointer = DB
        for c in word:
            if c not in pointer:
                pointer[c] = {'word': None}
            pointer = pointer[c]
        pointer['word'] = word

def game(board):
    score, longest, count = 0, 'Z', 0
    words = set()
    
    def check(r, c, pointer, board):
        nonlocal score, longest, count

        if pointer['word'] and pointer['word'] not in words:
            count += 1
            score += SCORE[len(pointer['word'])]
            words.add(pointer['word'])

        if len(pointer) != 1:
            for d in range(D):
                nr, nc = r+DR[d], c+DC[d]
                if nr==-1 or nr==WIDTH or nc==-1 or nc==WIDTH:
                    continue
                if board[nr][nc] not in pointer or traced[nr][nc]:
                    continue
                traced[nr][nc] = 1
                check(nr, nc, pointer[board[nr][nc]], board)
                traced[nr][nc] = 0

    def compare(x, y):
        if len(x) != len(y):
            return len(x)-len(y)
        else:
            return 1 if x<y else -1

    for r in range(WIDTH):
        for c in range(WIDTH):
            if board[r][c] in DB:
                traced[r][c] = 1
                check(r, c, DB[board[r][c]], board)
                traced[r][c] = 0

    return ' '.join((str(score), sorted(words, key=cmp_to_key(compare))[-1], str(count)))

# driver
dbInit()
for board in inputBoards():
    print(game(board))

