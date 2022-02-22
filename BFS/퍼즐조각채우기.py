# 참고 자료: https://devlibrary00108.tistory.com/608

from collections import defaultdict, deque

def solution(game_board, table):
    N = len(game_board)
    blocks = defaultdict(int)
    
    #블록 찾기 및 테이블 변환
    for i in range(N):
        for j in range(N):
            table[i][j] = (table[i][j] + 1) % 2
            if game_board[i][j] == 0:
                block = bfs(game_board, i, j, N)
                blocks[block] += 1
    return block_matching(blocks, table, N)

def bfs(traced, x, y, N):
    ret = [(0, 0)]
    q = deque()
    traced[x][y] = -1
    q.append((x, y, 0, 0))
    
    while q:
        x, y, pre_x, pre_y = q.popleft()
        cases = ((x+1, y, pre_x+1, pre_y), (x-1, y, pre_x-1, pre_y), 
                 (x, y+1, pre_x, pre_y+1), (x, y-1, pre_x, pre_y-1))
        for (nx, ny, n_pre_x, n_pre_y) in cases:
            if 0 <= nx < N and 0 <= ny < N and traced[nx][ny] == 0:
                traced[nx][ny] = -1
                q.append((nx, ny, n_pre_x, n_pre_y))
                ret.append((n_pre_x, n_pre_y))
    return tuple(ret)

def block_matching(blocks, table, N):
    answer = 0
    # 4방향으로 회전시켜 blanks 맞추기
    for _ in range(4):
        # 테이블을 회전한다.
        table = [list(row)[::-1] for row in zip(*table)]
        
        # traced checking을 위한 그래프 복제
        traced = [row[:] for row in table]

        for i in range(N):
            for j in range(N):
                if traced[i][j] == 0:
                    traced[i][j] = -1
                    block = bfs(traced, i, j, N)
                    if block in blocks:
                        answer += len(block)
                        blocks[block] -= 1
                        if not blocks[block]: del blocks[block]
                        # 블록 삭제 작업, 같은 블록을 trace하지 않게 삭제한다
                        table = [row[:] for row in traced]
                    else:
                        # 없으면 traced 초기화
                        traced = [row[:] for row in table]
    return answer