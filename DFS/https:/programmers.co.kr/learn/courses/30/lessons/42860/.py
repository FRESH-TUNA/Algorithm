answer = 1000000000
N, finish, traced = 0, 0, set()

def solution(name):
    global N, finish

    N = len(name)
    updown_answer = 0
    
    # up_down
    for idx, char in enumerate(name):
        updown_answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        if char != 'A': finish += 1
    if finish == 0: return 0
    if name[0] == 'A': finish += 1

    # dfs
    traced.add(0)
    dfs(name, 0, updown_answer)
    return answer

def dfs(name, cur_pos, cur):
    global answer

    if len(traced) == finish:
        answer = min(answer, cur)
        return

    for n in range(N):
        if n in traced or name[n] == 'A': continue
        
        n_cur = cur
        if cur_pos > n: n_cur += min(cur_pos-n, N-cur_pos+n)
        else: n_cur += min(n-cur_pos, cur_pos+N-n)
        if n_cur >= answer: continue
            
        traced.add(n)
        dfs(name, n, n_cur)
        traced.remove(n)
