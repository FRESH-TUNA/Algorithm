def solution(s):
    array = sorted([int(_s) for _s in s.split()])
    return str(array[0]) + " " + str(array[-1])
