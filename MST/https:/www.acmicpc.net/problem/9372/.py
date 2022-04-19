import sys

def init():
    input = sys.stdin.readline
    CASE_N = int(input())
    NN, NM, EDGES = [], [], []
    for _ in range(CASE_N):
        N, M = map(int, input().split())
        NN.append(N) 
        NM.append(M)
        EDGES.append([list(map(int, input().rstrip().split()))
                     for _ in range(NM[-1])])
    return CASE_N, NN, NM, EDGES

def solutions(CASE_N, NN, NM, EDGES):
    for N, M, EDGE in zip(NN, NM, EDGES): print(N-1)

if __name__ == '__main__':
    solutions(*init())
