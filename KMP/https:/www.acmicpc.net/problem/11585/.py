import sys, bisect, math

# global
N = None
S, P = None, None
LSP = None

def init():
    global N, S, P, LSP
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip().split() * 2
    P = input().rstrip().split()
    LSP = len(P) * [0]

def lsp():
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = LSP[j-1]
        if P[i] == P[j]: LSP[i] = j = j+1
    
def solution():
    res = i = j = 0

    while i < N*2-1:
        if S[i] == P[j]:
            i += 1
            j += 1
        elif j > 0: j = LSP[j-1]
        else: i += 1
        
        if j == len(P): 
            res += 1
            j = LSP[j-1]
    print(str(res // math.gcd(res, N)) + "/" 
         + str(N // math.gcd(res, N)))

init()
lsp()
solution()
