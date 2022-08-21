import sys

input = sys.stdin.readline
MAX = 50
N, M = map(int, input().split())
G = [list(input().rstrip()) for _ in range(N)]
D, DI, DJ = 3, [1,0,1], [0,1,1]
answer = 1

def check(n, m, CI, CJ):
    checked = True
    for d in range(D):
        CI[d] += DI[d]
        CJ[d] += DJ[d]

        if G[n][m] != G[CI[d]][CJ[d]]:
            checked = False
    return checked

def calculate(n, m):
    CI, CJ, result = [n,n,n], [m,m,m], 1

    for width in range(2, min(N-n+1, M-m+1)):
        if check(n, m, CI, CJ):
            result = width
    return result
    
for n in range(N):
    for m in range(M):
        answer = max(answer, calculate(n, m)**2)
print(answer)

