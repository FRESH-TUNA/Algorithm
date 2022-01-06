def solution(arr1, arr2):
    return [[sum(x[0] * x[1] for x in zip(R, C)) for C in zip(*arr2)] for R in arr1]
