import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
PARENT_INFO, PARENT_INFO[1], RANK = [0]*(N+1), 1, [1]*(N+1)

for n in range(N-1):
    PARENT_INFO[n+2] = int(input().rstrip())

PARENT = [n for n in range(N+1)]
REMOVE, QUERY = 0, 1
datas = [list(map(int, input().rstrip().split())) for _ in range(N-1+Q)][::-1]

def union(v1, v2):
    pv1, pv2 = parent(v1), parent(v2)
    if pv1 == pv2:
        return
    elif RANK[pv1] > RANK[pv2]:
        PARENT[pv2] = pv1
    elif RANK[pv1] < RANK[pv2]:
        PARENT[pv1] = pv2
    else:
        PARENT[pv2] = pv1
        RANK[pv1] += 1

def parent(node):
    if PARENT[node] != node:
        PARENT[node] = parent(PARENT[node])
    return PARENT[node]  

def add(node):
    parent = PARENT_INFO[node]
    PARENT[node] = parent

def query(node1, node2):
    return "YES" if parent(node1) == parent(node2) else "NO"

def solution():
    result = []
    for data in datas:
        if data[0] == REMOVE:
            union(data[1], PARENT_INFO[data[1]])
        else:
            result.append(query(data[1], data[2]))
    return result[::-1]
    
print('\n'.join(solution()))

