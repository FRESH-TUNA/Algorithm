answer = 1000000000
N, finish, traced = 0, 0, []

def solution(name):
    global N, finish, traced

    N = len(name)
    updown_answer = 0
    traced = [0] * len(name)
    
    # up_down
    for idx, char in enumerate(name):
        updown_answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        if char != 'A': finish += 1

    # dfs
    traced[0] = 1
    dfs(name, 0, 0, 1, updown_answer)
    return answer

def dfs(name, last_pos, cur_pos, depth, cur):
    global answer
    if depth == finish:
        answer = min(answer, cur)
        return

    for n in range(N):
        if traced[n] or name[n] == 'A': continue
            
        n_cur = cur
        if cur_pos > n: n_cur += min(cur_pos-n, N-cur_pos+n)
        else: n_cur += min(n-cur_pos, cur_pos+N-n)
        if n_cur >= answer: continue
            
        traced[n] = 1
        dfs(name, cur_pos, n, depth+1, n_cur)
        traced[n] = 0