import sys

# global
input = sys.stdin.readline
N, GRAPH = 0, []

def solution():
    for i in range(1, N):
        for j in range(1, i+2):
            GRAPH[i][j] += max(GRAPH[i-1][j], GRAPH[i-1][j-1])
    print(max(GRAPH[-1]))        
    
# driver
N = int(input())
GRAPH = [[0]+list(map(int, input().split()))+[0] 
         for _ in range(N)]
solution()