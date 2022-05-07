import sys
 
input = sys.stdin.readline
N, Datas = int(input()), []
for _ in range(N):
    input()
    Datas.append(list(map(int, input().split())))
    
def solution(data):
    n, p, res = len(data), len(data)-2, 0
 
    while p >= 0:
        while data[p] > 0 and data[p] >= data[p+1]:
            data[p] = data[p] // 2
            res += 1
        if data[p] == data[p+1]: return -1
        p -= 1
    return res
 
print('\n'.join(str(solution(d)) for d in Datas))
