import sys

def solution(classes, main, sub):
    db = [0] * (1000000+1)
    ans = 0

    for _class in classes:
        if db[_class]: 
            ans += db[_class]
            continue

        remain = _class - main
        _ans = 1
        
        if remain > 0:
            _ans, remain = _ans + remain // sub, remain % sub

        if remain > 0: _ans += 1

        db[_class] = _ans
        ans += db[_class]

    return ans
    


# driver
input = sys.stdin.readline
N = int(input())
classes = list(map(int, input().split()))
main, sub = map(int, input().split()[:2])
print(solution(classes, main, sub))
