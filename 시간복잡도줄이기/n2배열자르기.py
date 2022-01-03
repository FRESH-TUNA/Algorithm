def solution(n, left, right):
    return [x//n + 1 if x%n <= x//n else x%n + 1 for x in range(left, right + 1)]

# A divided
# B remaind

#if B < A + 1: A + 1
#else: B + 1

#A[6] = 3

#A = 6 // 4 = 1
#B = 6 % 4 = 2

#Z[7] = 4
#A = 7 // 4 = 1
#B = 7 % 4 = 3
#B + 1 = 4
