import sys
i = sys.stdin.readline

A , B = i().rstrip(), i().rstrip()
NA, NB = len(A), len(B)
DB = [[0]*(NB+1) for _ in range(NA+1)]

for i in range(NA):
    for j in range(NB):
        if A[i] == B[j]:
            DB[i+1][j+1] = DB[i][j]+1
        else:
            DB[i+1][j+1] = max(DB[i][j+1], DB[i+1][j])
print(DB[-1][-1])
