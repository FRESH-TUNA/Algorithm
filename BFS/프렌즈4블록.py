from collections import deque

def solution(m, n, board):
    answer = 0
    while True:
        return get_pung(m, n, board)
        #if not num: return answer
        #answer += num
        #shift(m, n, board)
    # 더해지는 값이 0일때 답을 반환하면 된다.
    return answer

# 탐색
def get_pung(m, n, board):
    traced, ans = [[0 for _ in range(n)] for _ in range(m)], 0
    for i in range(m):
        for j in range(n):
            if not traced[i][j]: ans += bfs(m, n, board, i, j, traced)
    return traced
    return ans

def bfs(m, n, board, root_i, root_j, traced):
    q, ans, root = deque([(root_i, root_j)]), 0, board[root_i][root_j]
    candids = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while q:
        i, j = q.pop()
        ans += 1
        
        # case 검사
        for (c_i, c_j) in [(i + _i, j + _j) for (_i, _j) in candids]:
            # in range 검사
            if not (c_i in range(m) and c_j in range(n)): continue
            # traced 검사 and root값 불일치 검사
            if traced[c_i][c_j] or board[c_i][c_j] != root: continue
            # 검사를 다 통과한후 insert
            traced[c_i][c_j] = 1
            q.appendleft((c_i, c_j))
        
    return ans if root != 0 else 0          
    

# dfs / bfs 끝난후 조정
# def shift():