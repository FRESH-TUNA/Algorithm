def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    answer = 0
    
    def union(x, y):
        x, y = parent(x), parent(y)
        x, y = max(x, y), min(x, y)
        parents[x] = y
    
    def parent(x):
        if parents[x] != x:
            parents[x] = parent(parents[x])
        return parents[x]

    for x, y, d in costs:
        if parent(x) == parent(y): continue
        answer += d
        union(x, y)
    return answer
