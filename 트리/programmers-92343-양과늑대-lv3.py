def solution(info, edges):
    visited, visited[0] = [0]*len(info), 1
    answer, GET = [1], 0
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer[GET] = max(answer[GET], sheep)
        else:
            return
        for i in range(len(edges)):
            parent, child = edges[i]
            isWolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(isWolf==0), wolf+(isWolf==1))
                visited[child] = 0
    dfs(1, 0)
    return answer[GET]

