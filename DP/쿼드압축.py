from collections import Counter

def solution(arr):
    ans = zzip(arr, *[len(arr) // 2] * 3)
    return [ans['0'], ans['1']]

def zzip(arr, x, y, w):
    cases = Counter()
    if w == 1:
        cases += Counter((str(arr[x][y]), str(arr[x-1][y]), 
                         str(arr[x][y-1]), str(arr[x-1][y-1])))
    else:
        w = w // 2
        for s in [zzip(arr, _x, _y, w) for (_x, _y) in 
            ((x-w, y-w), (x-w, y+w), (x+w, y-w), (x+w, y+w))]: 
            cases += Counter(s)

    return Counter(('1')) if not cases['0'] else (
        Counter(('0'))if not cases['1'] else cases)
