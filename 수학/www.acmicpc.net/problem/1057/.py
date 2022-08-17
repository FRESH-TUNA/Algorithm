def call():
    N, A, B = map(int, input().split())
    for round in range(N+1):
        if A == B:
            return round
        A, B = (A+1)//2, (B+1)//2
    return -1

print(call())

